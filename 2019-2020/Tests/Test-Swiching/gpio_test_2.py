import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM) # GPIO Numbers instead of board numbers
 
R1_GPIO = 17 # GPIO 17
GPIO.setup(R1_GPIO, GPIO.OUT) # GPIO Assign

GPIO.output(R1_GPIO, GPIO.LOW) # on
time.sleep(5) # wait 5 seconds
GPIO.output(R1_GPIO, GPIO.HIGH) # off