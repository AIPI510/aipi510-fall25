import serial
import time
import pandas as pd

# Sample data for testing (uncomment to bypass serial)
# sample_lines = [
#     "50000,0.0982,0.366,0.9216,-0.3418,-0.1099,0.1951,34.7547,-2.6229,25.9674,25.73,47.8,100.82,21.9,-5.3,354.9,510.97,-47.3",
#     "50200,0.0937,0.3668,0.9248,-0.2728,0.3367,-0.1321,36.7785,-2.5344,23.8479,25.68,47.9,100.8,22.0,-5.0,353.3,616.98,-35.3",
#     "50400,0.083,0.3715,0.9227,-0.1545,0.0868,-0.0353,34.413,-1.6637,26.3516,25.68,47.7,100.8,22.1,-5.0,355.4,314.02,-28.7",
#     "50600,0.0955,0.3653,0.9162,0.4666,-0.0624,-0.0407,38.7237,-2.5491,25.8837,25.75,47.9,100.81,21.7,-5.0,352.1,367.55,-41.4",
#     "50800,0.0904,0.3683,0.9188,0.4319,0.1481,-0.0388,38.5852,-3.6473,25.6772,25.68,47.7,100.83,21.9,-5.1,350.1,605.08,-30.4",
#     "51000,0.0898,0.3689,0.9176,-0.2906,0.011,-0.1093,35.5331,-2.0998,24.606,25.75,47.7,100.8,21.8,-5.1,350.1,631.25,-47.6",
#     "51200,0.0822,0.3648,0.9213,-0.3953,0.3225,0.003,37.5189,-2.3671,22.6783,25.71,48.0,100.81,21.6,-5.1,357.1,525.58,-25.2",
#     "51400,0.0853,0.3701,0.9214,0.4359,-0.1881,-0.1708,35.9451,-2.4098,24.4626,25.66,47.6,100.8,21.6,-5.4,351.9,354.47,-46.9",
#     "51600,0.0886,0.3727,0.9233,0.4527,0.1063,-0.0847,37.6551,-3.8001,26.3626,25.73,47.7,100.84,21.7,-5.0,349.6,452.56,-47.1",
#     "51800,0.0966,0.3633,0.9162,-0.3079,-0.1432,-0.1473,35.8298,-1.2259,24.7758,25.66,47.9,100.84,21.6,-5.4,356.3,495.42,-48.5"
# ]
# data = []
# for line in sample_lines[:10]:  # Use first 10
#     parts = line.split(',')
#     if len(parts) == 18:
#         entry = {
#             'time_ms': parts[0],
#             'ax_g': float(parts[1]),
#             'ay_g': float(parts[2]),
#             'az_g': float(parts[3]),
#             'gx_dps': float(parts[4]),
#             'gy_dps': float(parts[5]),
#             'gz_dps': float(parts[6]),
#             'hx_uT': float(parts[7]),
#             'hy_uT': float(parts[8]),
#             'mz_uT': float(parts[9])
#         }
#         data.append(entry)
# df = pd.DataFrame(data)
# df.to_csv('imu_data.csv', index=False)
# print(df.head(5))
# exit()

ser = serial.Serial('/dev/tty.usbmodem31301', 9600)
time.sleep(2)  # Wait for connection

data = []
for i in range(10):  # Read 10 lines
    line = ser.readline().decode('utf-8').strip()
    if line:  # Skip empty
        parts = line.split(',')
        if len(parts) == 18:  # Full line
            entry = {
                'time_ms': parts[0],
                'ax_g': float(parts[1]),
                'ay_g': float(parts[2]),
                'az_g': float(parts[3]),
                'gx_dps': float(parts[4]),
                'gy_dps': float(parts[5]),
                'gz_dps': float(parts[6]),
                'hx_uT': float(parts[7]),
                'hy_uT': float(parts[8]),
                'mz_uT': float(parts[9])
            }
            data.append(entry)

ser.close()

df = pd.DataFrame(data)
df.to_csv('imu_data.csv', index=False)
print(df.head(5))

# Captures IMU data (accel, gyro, mag) from Arduino.
# Parses ax/ay/az (g), gx/gy/gz (dps), hx/hy/mz (uT) into DataFrame.
# I plan to use this for hand gesture recognition to enable touchless controls, e.g., opening apps via specific motion thresholds.