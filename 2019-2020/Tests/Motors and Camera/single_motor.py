#from future import division
import time
import Adafruit_PCA9685
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

ch = 3# channel
#ch2 = 0
R1_GPIO = 17
GPIO.setup(R1_GPIO, GPIO.OUT)

power = int(input("On(1)/Off(0):"))
if power == 1:
    GPIO.output(R1_GPIO, GPIO.HIGH)
if power == 0:
    GPIO.output(R1_GPIO, GPIO.LOW)

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)
pwm.set_pwm(ch, 0, 409) # channel 0, 0 through motor_pwm (0~4095)
#pwm.set_pwm(ch2, 0, 409)
#pwm.set_pwm(ch+1, 0, 409)
print("Maks verildi, gücü ver")
#pwm.stop() # channel 0, 0 through motor_pwm (0~4095)
x=311
while x!=10:
    print("cıkmak icin x = 10")
    x = int(input("Enter x:"))
    pwm.set_pwm(ch, 0, x)
    #pwm.set_pwm(ch2, 0, x)
    #pwm.set_pwm(ch+1, 0, x)

pwm.set_pwm(ch, 0, 311)
#pwm.set_pwm(ch2, 0, 311)
#pwm.set_pwm(ch+1, 0, x)
time.sleep(1)
GPIO.output(R1_GPIO, GPIO.LOW)
