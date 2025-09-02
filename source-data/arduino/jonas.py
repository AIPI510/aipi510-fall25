import serial
import time

ser = serial.Serial('/dev/tty.usbmodem31301', 9600)
time.sleep(2)  # Wait for connection

# for i in range(10):  # Read 10 lines
#     line = ser.readline().decode('utf-8').strip()
    # print(line)

# ser.close()

data = []

for i in range(10):  # Read 10 lines
    line = ser.readline().decode('utf-8').strip()
    parts = line.split(',')
    if len(parts) == 18:
        entry = {
            'key': parts[0],
            'value1': parts[1],
            'value2': float(parts[2])
        }
        data.append(entry)

        if len(data) == 5:
            print(data)
            break
