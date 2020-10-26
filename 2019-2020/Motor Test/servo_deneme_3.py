import time
import Adafruit_PCA9685
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM) #switching
S_GPIO=17
GPIO.setup(S_GPIO, GPIO.OUT)

pwm =Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)
x=350
GPIO.output(S_GPIO,GPIO.HIGH)
while x != 10:
    
    x=int(input("Enter (break 10), 150-600: "))
    pwm.set_pwm(10,0,x)



GPIO.output(S_GPIO,GPIO.LOW)