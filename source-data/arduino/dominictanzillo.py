import serial
import time
ser = serial.Serial('/dev/tty.usbmodem1101', 9600)  # Replace with your port, Run in terminal:ls /dev/tty.*
time.sleep(2)  # Wait for connection
for i in range(10):  # Read 10 lines
    line = ser.readline().decode('utf-8').strip()
    print(line)
ser.close()

data = {
    46100: [0.0895, 0.3708, 0.9208, -0.49, 0.06, 0.00, 39.00, -1.00, 27.00, 25.71, 47.9, 100.82, 21.9, -5.2, 358.5, 111.0, -49.4],
    46311: [0.0918, 0.3678, 0.9224, -0.06, 0.12, -0.06, 38.00, -2.00, 24.00, 25.70, 47.9, 100.82, 21.7, -5.3, 357.0, 154.2, -46.5],
    46523: [0.0961, 0.3676, 0.9231, 0.06, 0.00, 0.06, 36.00, -4.00, 24.00, 25.70, 47.8, 100.82, 21.7, -5.5, 353.7, 323.6, -40.1],
    46735: [0.0914, 0.3698, 0.9213, -0.12, 0.12, 0.00, 37.00, -5.00, 25.00, 25.70, 47.8, 100.82, 21.9, -5.3, 352.3, 282.9, -41.3],
    46946: [0.0931, 0.3676, 0.9227, -0.12, 0.12, 0.00, 38.00, -5.00, 30.00, 25.68, 47.8, 100.82, 21.7, -5.4, 352.5, 191.1, -44.7],
    47157: [0.0920, 0.3683, 0.9208, -0.24, 0.18, 0.00, 36.00, -2.00, 26.00, 25.70, 47.7, 100.82, 21.8, -5.3, 356.8, 197.8, -44.4],
    47369: [0.0924, 0.3677, 0.9231, -0.12, 0.06, -0.06, 34.00, -5.00, 24.00, 25.70, 47.7, 100.82, 21.7, -5.3, 351.6, 1620.1, -26.1],
    47580: [0.0914, 0.3677, 0.9216, -0.24, 0.18, -0.06, 35.00, -3.00, 24.00, 25.68, 47.8, 100.82, 21.7, -5.3, 355.1, 2330.2, -23.0],
    47792: [0.0927, 0.3685, 0.9203, -0.24, 0.12, 0.00, 37.00, -4.00, 23.00, 25.68, 48.0, 100.82, 21.8, -5.3, 353.8, 904.4, -31.2],
    48003: [0.0927, 0.3688, 0.9200, -0.31, 0.06, -0.06, 35.00, -4.00, 25.00, 25.70, 48.2, 100.82, 21.8, -5.3, 353.5, 109.4, -49.5]
}
### This data is providing location and rotational data (telemetry data), in addition to temperature humidity, barometric pressure and even a PDM microphone. This information is essential for rocketry and modelling the location of the rocket live while communicating with the system.
### This is the Nano 33 Sense REV2 and provides all the telemetry data and could be used on a variety of devices and applications.
### It could also be applied to phyiscal data for people.

#include "Arduino_BMI270_BMM150.h"  // IMU (accel, gyro, mag)
#include <Arduino_HS300x.h>         // ✅ HS3003 on Rev2 (temp & humidity)
#include <Arduino_LPS22HB.h>        // Barometric pressure
#include <PDM.h>                    // PDM microphone