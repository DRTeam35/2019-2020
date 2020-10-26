import serial
ser = serial.Serial('/dev/ttyUSB0', 9600)
i = 0
while True:
    read_serial = ser.readline()
    print(read_serial)
    i = i + 1
    print(i)