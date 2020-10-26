import time
#from future import division
import Adafruit_PCA9685

pwm = Adafruit_PCA9685.PCA9685()

servo_min = 150
servo_max = 600
servo_mid = 350

pwm.set_pwm_freq(50)
x = 11
while x != 10:
    x = int(input("Enter x: "))
    pwm.set_pwm(10, 0, x)
    time.sleep(1)

