import serial
import time
import pandas as pd

# Step 5: connect to Arduino (replace with your actual port)
ser = serial.Serial('/dev/tty.usbmodemXXXX', 9600)
time.sleep(2)  # wait for Arduino to reset

data = []

# Read 20 lines of sensor data
for i in range(20):
    line = ser.readline().decode('utf-8').strip()
    # Assume Arduino sends comma-separated values: "temperature,light,motion"
    parts = line.split(",")
    if len(parts) == 3:
        try:
            temperature = float(parts[0])
            light = float(parts[1])
            motion = int(parts[2])
            data.append({"temperature": temperature, "light": light, "motion": motion})
        except ValueError:
            continue

ser.close()

# Convert to DataFrame
df = pd.DataFrame(data)

# Step 7: print first 5 rows
print(df.head())

# Step 6: save to CSV
df.to_csv("arduino_data.csv", index=False)

# Step 8: notes
"""
Notes:
This dataset was collected from Arduino Nano 33 BLE Sense sensors:
- Temperature (°C), Light (lux), Motion (binary flag).
The data can be used to monitor environmental conditions,
detect movement, and analyze changes over time.
"""

