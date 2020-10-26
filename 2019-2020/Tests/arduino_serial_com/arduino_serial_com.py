import serial
ser = serial.Serial('/dev/ttyAMA0', 9600, timeout=1)
ser.open()

ser.write("testing")
try:
    while 1:
        response = ser.readline()
        print response
except KeyboardInterrupt:
    ser.close()


##############
servo_min = 150
servo_max = 600
servo_mid = 350

pwm.set_pwm_freq(50)

pwm.set_pwm(8, 0, servo_mid)
time.sleep(1)
################