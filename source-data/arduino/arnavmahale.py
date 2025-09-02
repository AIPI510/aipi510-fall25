import serial
import time
import pandas as pd

ser = serial.Serial('/dev/tty.usbmodem2101', 9600)  # Replace with your port

time.sleep(2)  # Wait for connection

sensor_data = []

for i in range(10):  # Read 10 lines
    line = ser.readline().decode('utf-8').strip()
    sensor_data.append([line])

ser.close()

df = pd.DataFrame(sensor_data)
print(df.head())

##################################
# This script reads serial data from Arduino Nano 33 BLE Sense Rev2.
# The output data from the sensor is structured into a DataFrame.
# This data can be used for monitoring environment changes or feeding ML models.
##################################