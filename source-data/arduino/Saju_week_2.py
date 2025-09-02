import serial
import time
ser = serial.Serial('COM3', 9600)  # Replace with your port
time.sleep(2)  # Wait for connection
for i in range(10):  # Read 10 lines
    line = ser.readline().decode('utf-8').strip()
    print(line)
ser.close()

#I used GitHub copilot to help me figure out why serial isn't working and to help me with the virtual enviroment. 9/02/2025.