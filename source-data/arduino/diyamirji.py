#diyamirji.py

import serial
import time
import pandas as pd

ser = serial.Serial('/dev/tty.usbmodem14401', 9600)  # Replace with your port, Run in terminal:ls /dev/tty.*
time.sleep(2)  # Wait for connection
lst = []
for i in range(10):  # Read 10 lines
    line = ser.readline().decode('utf-8').strip()
    line_list = line.split(", ")
    lst.append(line_list)
ser.close()
df = pd.DataFrame(lst)
print(df.head())

# I would use the tempC sensor data
# I would use this data to give a recommendation of what clothes to wear 
# based on what the temperature returned was
# ex: lower tempC would tell the user to wear a thicker jacket
