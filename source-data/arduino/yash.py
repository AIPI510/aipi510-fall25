import serial
import time
import pandas

ser = serial.Serial('/dev/tty.usbmodem101', 9600)
time.sleep(2)

output = []

for i in range(10):
    line = ser.readline().decode('utf-8').strip()

    print(line)
    output.append(line)
ser.close()

df = pandas.DataFrame({'output': output})

print(df.iloc[:5])

# NANO-33-BLE-SENSE-REV2 sensor
