import time
import Adafruit_PCA9685
import RPi.GPIO as GPIO

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)
GPIO.setmode(GPIO.BCM)
S_GPIO = 17
GPIO.setup(S_GPIO, GPIO.OUT) # GPIO Assign mode

power = int(input("Power on(1) / off(0)?"))
if power == 1:
  GPIO.output(S_GPIO, GPIO.HIGH) # on
if power == 0:
  GPIO.output(S_GPIO, GPIO.LOW) # out

# 0 through motor_pwm (0~4095) for PCA                     
#pwm.set_pwm(channel, start Duty Cycle, End Duty Cycle)
                       # Dikey/Yatay,  Ön/Arka
pwm.set_pwm(0, 0, 409) #  
pwm.set_pwm(1, 0, 409) #  
pwm.set_pwm(2, 0, 409) # 
pwm.set_pwm(3, 0, 409) # 
pwm.set_pwm(4, 0, 409) # 
pwm.set_pwm(5, 0, 409) # 
pwm.set_pwm(6, 0, 409) # 
pwm.set_pwm(7, 0, 409) #  

print("Maks verildi, dewamke, ilk önce x'e 311 ver, motorlar ses versin")
x = int(input("Enter x:"))
pwm.set_pwm(0, 0, x) 
pwm.set_pwm(1, 0, x)  
pwm.set_pwm(2, 0, x) 
pwm.set_pwm(3, 0, x) 
pwm.set_pwm(4, 0, x) 
pwm.set_pwm(5, 0, x) 
pwm.set_pwm(6, 0, x-1) 
pwm.set_pwm(7, 0, x)  

x = 311
mode = 4 # initialize the mode
while mode!=10:
  print("cikmak icin mode = 10")
  mode = int(input("Enter mode, Yukari/Asagı(1), Ileri/Geri(2), Sag(3), Sol(4):"))


  if mode == 1: # YUKARI/ASAGI
    x = 311
    while x!= 10:
      print("cikmak icin x = 10")
      x = int(input("Enter x:"))
      # Dikey Motorlar
      pwm.set_pwm(0, 0, x) 
      pwm.set_pwm(1, 0, x)  
      pwm.set_pwm(2, 0, x) 
      pwm.set_pwm(3, 0, x) 

  if mode == 2: # ILERI/GERI
    x = 311
    while x!= 10:
      print("cikmak icin x = 10")
      x = int(input("Enter x:"))
      # Yatay Motorlar
      pwm.set_pwm(4, 0, x+15) 
      pwm.set_pwm(5, 0, x)  
      pwm.set_pwm(6, 0, x+14) 
      pwm.set_pwm(7, 0, x) 

  if mode == 3: # SAG/SOL
    x = 311
    # sol ön ile sağ arka düz çalışırken, sağ ön ile sol arka ters çalışacak
    while x!= 10:
      print("cikmak icin x = 10")
      x = int(input("Enter x:"))
      f = x - 311
      pwm.set_pwm(4, 0, x) 
      pwm.set_pwm(7, 0, x-2*f)  
      #pwm.set_pwm(?, 0, x) 
      #pwm.set_pwm(?, 0, x)
  
  

pwm.set_pwm(0, 0, 311) 
pwm.set_pwm(1, 0, 311)  
pwm.set_pwm(2, 0, 311) 
pwm.set_pwm(3, 0, 311) 
pwm.set_pwm(4, 0, 311) 
pwm.set_pwm(5, 0, 311) 
pwm.set_pwm(6, 0, 310) 
pwm.set_pwm(7, 0, 311)  

time.sleep(1)
GPIO.output(S_GPIO, GPIO.LOW) # out

print("Helalkee Menekse <3 ")
