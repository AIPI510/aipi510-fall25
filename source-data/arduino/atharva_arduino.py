import serial
import time
import pandas as pd

ser = serial.Serial('/dev/tty.usbmodemXXXX', 9600)  # Replace with your port
serial_values = []
time.sleep(2)  # Wait for connection
for i in range(10):  # Read 10 lines
    line = ser.readline().decode('utf-8').strip()
    print(line)
    serial_values.append(line)

df = pd.DataFrame(serial_values)
print(df.head())

ser.close()