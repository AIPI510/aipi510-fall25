import serial
import pandas as pd
import time
ser = serial.Serial('/dev/tty.usbmodem1301', 9600)  # Replace with your port
time.sleep(2)  # Wait for connection

lines =[]
for i in range(10):  # Read 10 lines
    line = ser.readline().decode('utf-8').strip()

    lines.append(line)

df = pd.DataFrame(lines)
# print(df.shape())
# headers = ["time_ms", "ax_g", "ay_g", "az_g", "gx_dps", "gy_dps", "gz_dps", "mx_uT", "my_uT", "mz_uT", "temp_C", "hum_pct", "press_hPa", "roll_deg", "pitch_deg", "heading_deg", "mic_rms", "mic_dBFS"]
# df.columns = headers
print(df[:5])
print(df.info(), df.describe())
df.to_csv("alex.csv")
ser.close()

# there is time, axis, temperature, humidity, pressure, and rotation data. I could use the arduino to learn about its environment in a physical experiment
