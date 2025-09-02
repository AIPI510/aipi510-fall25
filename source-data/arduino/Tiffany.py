import serial
import time
import pandas as pd

ser=serial.Serial("COM3", 9600)  # open serial port
time.sleep(2)  # wait for the serial connection to initialize
lines = []
for i in range(10):
    line = ser.readline().decode('utf-8').rstrip()
    lines.append(line)
# Create a DataFrame with one column 'line' and each row as a line read
data = pd.DataFrame({'line': lines})
#The above code snippet was generated using Copilot, an AI coding assistant

print(data)
ser.close()
