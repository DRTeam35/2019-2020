import RPi.GPIO as GPIO
import time

servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(2.5) # Initialization
try:
  while True:
    #p.ChangeDutyCycle(0)
    #time.sleep(1)
    #p.ChangeDutyCycle(5)
    #print("2.5")
    #time.sleep(1)
    
    
    p.ChangeDutyCycle(5)
    print("5")
    time.sleep(1)
    p.ChangeDutyCycle(6.5)
    print("6.5")
    time.sleep(1)
    p.ChangeDutyCycle(8)
    print("8")
    time.sleep(1)
    
    
    #p.ChangeDutyCycle(12.5)
    #print("12.5")
    #time.sleep(1)
    #p.ChangeDutyCycle(10)
    #print("10")
    #time.sleep(1)
    #p.ChangeDutyCycle(7.5)
    #print("7.5")
    #time.sleep(1)
    #p.ChangeDutyCycle(5)
    #print("5")
    #time.sleep(1)
    #p.ChangeDutyCycle(2.5)
    #print("2.5")
    #time.sleep(1)
    #p.ChangeDutyCycle(0)
    #time.sleep(1)
except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()