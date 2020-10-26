from picamera import PiCamera
from time import sleep
import RPi.GPIO as GPIO
import time

camera = PiCamera()
camera.rotation = 180

camera.start_preview()

servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(2.5) # Initialization
try:
  while True:  
    
    p.ChangeDutyCycle(5)
    print("5")
    time.sleep(1)
    p.ChangeDutyCycle(6.5)
    print("6.5")
    time.sleep(1)
    p.ChangeDutyCycle(8)
    print("8")
    time.sleep(1)

except KeyboardInterrupt:
  camera.stop_preview()
  p.stop()
  GPIO.cleanup()
