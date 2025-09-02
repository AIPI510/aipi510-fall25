import serial
import time
import pandas as pd

ser = serial.Serial('COM7', 9600)  # Use your Arduino's COM port
time.sleep(2)  # Allow time for Arduino reset

arduino_dict = {
    'Timestamp':[], 'Accelerometer_X':[], 'Accelerometer_Y':[], 'Accelerometer_Z':[],
    'Gyroscope_X':[], 'Gyroscope_Y':[], 'Gyroscope_Z':[],
    'Magnetometer_X':[], 'Magnetometer_Y':[], 'Magnetometer_Z':[],
    'Temperature':[], 'Humidity':[], 'Pressure':[], 'Secondary_Temperature':[],
    'Roll':[], 'Pitch':[], 'Yaw':[], 'Other_orientation':[]
}

for _ in range(10):  # Read 10 lines
    line = ser.readline().decode('utf-8').strip()
    split_line = line.split(',')
    print(split_line)
    
    for idx, key in enumerate(arduino_dict.keys()):
        if idx < len(split_line):
            try:
                value = float(split_line[idx].strip())
            except ValueError:
                value = None
            arduino_dict[key].append(value)
        else:
            arduino_dict[key].append(None)

ser.close()

df = pd.DataFrame(arduino_dict)
print(df)

#This was the arudino task. I essentially read in the data and asked chatgpt what the data actualy represented by putting in the exact board.
#I found the variables that the data represented and created a dictionary where the keys are the variables and the values are empty lists
#I then put in the information from the ten lines into these lists and crated a dataframe from the dictionary at the end

