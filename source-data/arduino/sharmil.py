import serial.tools.list_ports

# Install pyserial
# Identify the serial port Arduino is connected to
"""
ports = serial.tools.list_ports.comports()
for port in ports:
    print(f"Device: {port.device} — Description: {port.description}")
O/P: Device: COM3 — Description: USB Serial Device (COM3)
"""
import serial
import time
import pandas as pd
# Connect to serial port (change this to match your actual port)
ser = serial.Serial("COM3", 9600) 
# Collect lines of data
data_list = []
time.sleep(2)  # Wait for connection


# 1. Define the column names (you can rename these based on what each value means)
columns = [
    "timestamp", "acc_x", "acc_y", "acc_z", "gyro_x", "gyro_y", "gyro_z",
    "mag_x", "mag_y", "mag_z", "temp", "humidity", "pressure",
    "angle_x", "angle_y", "heading", "distance", "altitude"
]

for _ in range(10):  # Read 10 lines
    line = ser.readline().decode('utf-8').strip()
    print("Raw:", line)

    try:
        values = [float(x) for x in line.split(',')]
        if len(values) == len(columns):
            data_list.append(dict(zip(columns, values)))
        else:
            print("⚠️ Skipped malformed row")
    except Exception as e:
        print("⚠️ Parsing error:", e)

ser.close()

# 4. Convert to DataFrame
df = pd.DataFrame(data_list)

# 5. Print the first 5 rows
print("\nFirst 5 rows:")
print(df.head())

# 6. Save to CSV
df.to_csv("sensor_data.csv", index=False)

# 7. Notes
"""
NOTES:
- This script reads 10 lines of real-time sensor data from an Arduino or similar device via Serial.
- The sensor bundle includes accelerometer, gyroscope, magnetometer, temperature, humidity, and pressure.
- This data can be used for motion tracking, orientation estimation, environment sensing, or AI training.
- Portions of this script were generated using OpenAI's ChatGPT (GPT-4) to assist with API integration, data parsing, and Python scripting.
"""
