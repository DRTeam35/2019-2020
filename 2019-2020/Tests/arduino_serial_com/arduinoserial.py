import serial
import time
ser = serial.Serial('/dev/ttyAMA0', 9600, timeout=1)
ser.close()
time.sleep(1)
ser.open()

ser.write(b"testing")
try:
    while 1:
        response = ser.readline()
        print(response)
except KeyboardInterrupt:
    ser.close()