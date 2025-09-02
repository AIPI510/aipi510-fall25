import serial
import time
import pandas as pd

ser = serial.Serial('/dev/tty.usbmodem11301', 9600)  # Replace with your port
data=[]
time.sleep(2)  # Wait for connection
for i in range(10):  # Read 10 lines
    line = ser.readline().decode('utf-8').strip()
    print(line)
    data.append(line)

df = pd.DataFrame(data, columns= [
    "time_ms",
    "accel_x_g", "accel_y_g", "accel_z_g",
    "gyro_x_dps", "gyro_y_dps", "gyro_z_dps",
    "mag_x_uT", "mag_y_uT", "mag_z_uT",
    "temperature_C", "humidity_percent", "pressure_hPa",
    "roll_deg", "pitch_deg", "heading_deg",
    "mic_rms"
])
df.dropna(inplace=True)
print(df.head(5))
ser.close()