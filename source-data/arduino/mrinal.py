import serial
import time
import pandas as pd
ser = serial.Serial('/dev/tty.usbmodem101', 9600)  # Replace with your port, Run in terminal:ls /dev/tty.*
lst = []
time.sleep(2)
for i in range(10):
    line = ser.readline().decode('utf-8').strip()
    lst.append(line)
    df = pd.DataFrame(lst, columns=["data"])
    print(df.head())
ser.close()

'''
The data I have is from a sensor that stores accelaration, gyro and magentic fields. 
I could use this data to detect anamolies and predict natural calamities. 
'''
