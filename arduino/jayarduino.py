import serial
import time
import pandas as pd


ser = serial.Serial('/dev/tty.usbmodem1301', 9600)  
time.sleep(2)  

data = []
for i in range(10):  
    line = ser.readline().decode('utf-8').strip()
    print("Raw:", line)

   
    values = [float(x) for x in line.split(",") if x.strip() != ""]
    data.append(values)

ser.close()


df = pd.DataFrame(data)


df.to_csv("sensor_data.csv", index=False)


print("\nFirst 5 rows of collected data:")
print(df.head())

# notes
# this script reads sensor data from an Arduino
# arduino was programmed to stream temperature and light values.
# the script parses each line into a structured dictionary, then saves to CSV
# in a real project, this data could be used for monitoring room environment.

