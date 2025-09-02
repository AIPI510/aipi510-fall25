import serial

import time

import pandas as pd

ser = serial.Serial('COM3', 9600) # Replace with your port

time.sleep(2) # Wait for connection

lines = []

for i in range(10): # Read 10 lines
    
    line = ser.readline().decode('utf-8').strip()

    print(line)

    # Parse output into a list
    lines.append(line)

# Save to DataFrame
data_df = pd.DataFrame(lines)

# Print the first 5 rows
print(data_df.head())

ser.close()

"""
Notes: The sensor I used is the Arduino Nano 33 BlE SENSE REV2 sensor. I would use this data to report real-time 
information that the sensor is providing such as temperature, light, and movement (as noted by the instructions sheet),
primarily in a web application.
"""