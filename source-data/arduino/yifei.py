import os
import re
import json
import time
import serial
import pandas as pd
from serial.tools import list_ports


ser = serial.Serial('COM3', 9600)  # Replace with your port
time.sleep(2)  # Wait for connection
for i in range(10):  # Read 10 lines
    line = ser.readline().decode('utf-8').strip()
    print(line)
ser.close()

def autodetect_arduino_port(preferred=None):
    """Return a likely Arduino serial port or the preferred one if provided."""
    if preferred:
        return preferred
    for p in list_ports.comports():
        name = (p.device or "").lower()
        desc = (p.description or "").lower()
        if any(k in desc for k in ["arduino", "nano", "usb serial"]) or \
           any(k in name for k in ["usbmodem", "ttyacm", "com"]):
            return p.device
    return None


def try_num(s):
    """Best-effort convert string to int/float; otherwise return original text."""
    if s is None:
        return None
    s = str(s).strip()
    if s.lower() in {"nan", "null"}:
        return None
    try:
        if re.search(r"[.\deE+-]", s) and any(ch in s for ch in ".eE"):
            return float(s)
        return int(s)
    except Exception:
        return s


def parse_line_to_dict(line):
    """
    Parse one serial text line into a dict.
    Priority: JSON -> key/value pairs -> comma-separated values.
    """
    s = line.strip()
    if not s:
        return None

    # 1) JSON object/array
    try:
        obj = json.loads(s)
        if isinstance(obj, dict):
            return {k: try_num(v) for k, v in obj.items()}
        if isinstance(obj, list):
            return {f"v{i}": try_num(v) for i, v in enumerate(obj)}
    except Exception:
        pass

    # 2) key=value or key:value pairs separated by comma/space
    tokens = re.split(r"[,\s]+", s)
    kv = {}
    for tok in tokens:
        if not tok:
            continue
        if "=" in tok:
            k, v = tok.split("=", 1)
        elif ":" in tok:
            k, v = tok.split(":", 1)
        else:
            # bare token -> assign to next valueN
            k, v = f"value{len(kv)}", tok
        kv[k.strip()] = try_num(v.strip())
    if kv:
        return kv

    # 3) plain comma-separated values
    if "," in s:
        parts = [p.strip() for p in s.split(",")]
        return {f"v{i}": try_num(v) for i, v in enumerate(parts)}

    # 4) fallback: put raw text
    return {"raw": s}


def read_serial_rows(port="COM3", baud=9600, lines=100, timeout=2.0):
    """Read `lines` lines from serial and return a DataFrame."""
    # Allow auto-detection if a user didn't pass a port explicitly
    if port is None:
        port = autodetect_arduino_port()

    ser = serial.Serial(port, baud, timeout=timeout)
    time.sleep(2)  # wait for the board to reset/open

    rows = []
    for _ in range(lines):
        raw = ser.readline().decode("utf-8", errors="ignore").strip()
        if not raw:
            continue
        d = parse_line_to_dict(raw)
        if d:
            d["_ts"] = time.time()     # Unix timestamp for later plotting
            d["_raw"] = raw            # keep raw text for traceability
            rows.append(d)

    ser.close()
    return pd.DataFrame(rows)


if __name__ == "__main__":
    # Adjust baud to match your Arduino sketch if needed (e.g., 115200).
    df = read_serial_rows(port="COM3", baud=9600, lines=150)

    if df.empty:
        print("No data parsed. Check port/baud or your Arduino print format.")
    else:
        # 7) Print first 5 rows
        print(df.head())

        # Save CSV
        os.makedirs("data", exist_ok=True)
        out_path = "data/arduino_readings.csv"
        df.to_csv(out_path, index=False)
        print(f"Saved {len(df)} rows to {out_path}")

    """
    Notes:
    - Hardware: Arduino Nano 33 BLE Sense Rev2 streaming sensor lines over Serial (9600 baud).
    - Parsing: try JSON first; otherwise parse key/value pairs (e.g., ax=..., ay=..., temp: 24.3),
      else treat comma-separated values as v0, v1, ...
    - Output: Structured pandas DataFrame + CSV at data/arduino_readings.csv, with _ts timestamp and _raw original text.
    - Possible uses: visualize time series (temperature/light/accel), compute moving averages, detect thresholds or motion events.
    - Tips: Close Arduino Serial Monitor before running; ensure the baud rate matches Serial.begin(...) in your sketch.
    """