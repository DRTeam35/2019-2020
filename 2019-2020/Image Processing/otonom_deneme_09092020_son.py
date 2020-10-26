# image processing lib.
import cv2
import numpy as np
# motor control lib.
import time
import Adafruit_PCA9685
# switching lib.
from time import sleep
import RPi.GPIO as GPIO

# from picamera import PiCamera

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)  # freq of the motors 50/60 Hz

# power switching on/off
S_GPIO = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(S_GPIO, GPIO.OUT)  #high/low of gpio
time.sleep(1)
GPIO.output(S_GPIO, GPIO.HIGH)

def motor_fr(p):  # ileri/geri motorlar
    print("ileri/geri calisiyor")
    pwm.set_pwm(4, 0, p)
    pwm.set_pwm(5, 0, p)
    pwm.set_pwm(6, 0, p)
    pwm.set_pwm(7, 0, p)


def motor_ud(p):  # yukarı/aşağı motorlar
    print("yukari/asagi calisiyor")
    pwm.set_pwm(0, 0, p)
    pwm.set_pwm(1, 0, p)
    pwm.set_pwm(2, 0, p)
    pwm.set_pwm(3, 0, p)

def motor_r_yengec(p):  # sağ/sol motorlar
    #################################
    fark = p - 311
    pwm2 = 311 - fark
    pwm.set_pwm(4, 0, pwm2-5)
    pwm.set_pwm(5, 0, p+5)
    pwm.set_pwm(6, 0, p+10)
    pwm.set_pwm(7, 0, pwm2-10)


def motor_l_yengec(p):  # sağ/sol motorlar
    #################################
    fark = p - 311
    pwm2 = 311 - fark
    pwm.set_pwm(4, 0, p+5)
    pwm.set_pwm(5, 0, pwm2-5)
    pwm.set_pwm(6, 0, pwm2-10)
    pwm.set_pwm(7, 0, p+10)

# def motor_rl(p):  # sağ/sol motorlar
#     #################################
#     print("sag/sol gidis calisiyor")
#     pwm.set_pwm(4, 0, p)
#     pwm.set_pwm(5, 0, p)
#     pwm.set_pwm(6, 0, p)
#     pwm.set_pwm(7, 0, p)

def motor_stp():  # motorları durdur
    pwm.set_pwm(0, 0, 311)  # sağ ön dikey
    pwm.set_pwm(1, 0, 311)  # sol ön dikey
    pwm.set_pwm(2, 0, 311)  # sağ arka dikey
    pwm.set_pwm(3, 0, 311)  # sol arka dikey
    pwm.set_pwm(4, 0, 311)  # sağ ön itici
    pwm.set_pwm(5, 0, 311)  # sol ön itici
    pwm.set_pwm(6, 0, 310)  # sağ arka itici
    pwm.set_pwm(7, 0, 311)  # sol arka itici
    time.sleep(1)


def motor_r_donus(p):
    fark = p - 311
    pwm2 = 311 - fark
    pwm.set_pwm(4, 0, pwm2)
    # pwm.set_pwm(5, 0, pwm)
    # pwm.set_pwm(6, 0, fark)
    pwm.set_pwm(7, 0, p)


def motor_l_donus(p):
    fark = p - 311
    pwm2 = 311 - fark
    pwm.set_pwm(4, 0, p)
    # pwm.set_pwm(5, 0, pwm)
    # pwm.set_pwm(6, 0, fark)
    pwm.set_pwm(7, 0, pwm2)

def ilk_deneme():
    print("ilk deneme calisiyor")
    motor_stp()

    # 5 saniye ileri
    motor_fr(int(350))
    time.sleep(5)
    motor_stp()

    # tek sağa dönüş komutu
    motor_r_donus(350)
    time.sleep(2)
    motor_stp()

    # tek sola dönüş komutu
    motor_l_donus(350)
    time.sleep(2)
    motor_stp()

    # 2 saniye yukarı
    motor_ud(330)
    time.sleep(2)
    motor_stp()

    # 1 saniye aşağı
    motor_ud(290)
    time.sleep(1)
    motor_stp()

    #3 saniye sağa gidiş
    motor_rl(350)
    time.sleep(3)
    motor_stp()

    #3 saniye sola gidiş
    motor_rl(270)
    time.sleep(3)
    motor_stp()

def arama_deneme():
    print("arama deneme calisiyor")
    motor_stp()
    #3 (r_t) saniye ileri
    motor_fr(340)
    time.sleep(3)
    motor_stp()
    #90 derece sağa dönüş
    motor_r_donus(330)
    time.sleep(2)
    motor_stp()

    #1 saniye ileri
    motor_fr(330)
    time.sleep(1)
    motor_stp()

    #90 derece sağa dönüş
    motor_r_donus(330)
    time.sleep(2)
    motor_stp()

    #3 (r_t) saniye ileri
    motor_fr(340)
    time.sleep(3)
    motor_stp()

    #90 derece sağa dönüş
    motor_r_donus(330)
    time.sleep(2)
    motor_stp()

    #2 saniiye ileri
    motor_fr(340)
    time.sleep(2)
    motor_stp()

    #90 derece sağa dönüş
    motor_r_donus(330)
    time.sleep(2)
    motor_stp()

    #3 (r_t) saniye ileri
    motor_fr(340)
    time.sleep(3)
    motor_stp()

    #bulamadı yukarı çık
    motor_ud(330)
    time.sleep(2)
    motor_stp()

motor_stp() # motor initialization
time.sleep(4) # wait for the motor calibration

x = 1
y = 1
while x != 10:
    x = int(input("Enter x: "))
    
    motor_ud(280)  # hızlı iniyor
    time.sleep(1)
    motor_stp()

    for i in range(0, 4):  # 6m gitmiş oldu, havuzu ortaladı
        motor_fr(330)
        time.sleep(3)
        motor_stp()

    motor_ud(280)  # hızlı iniyor
    time.sleep(2)
    motor_stp()

    #y = int(input("Enter y: "))
    #motor_ud(0)
    #time.sleep(3)
    #motor_l_yengec(x)
    #time.sleep(y)
    #motor_r_yengec(x)
    #time.sleep(1)
    #motor_stp()
    
    #motor_fr(340)
    #time.sleep(3)
    #motor_stp()
    
    #motor_ud(280)
    #time.sleep(2)

### bu bir
#    motor_r_yengec(330)
#    time.sleep(2.5)
#    motor_stp()
#    
#    motor_r_yengec(330)
#    time.sleep(2.5)
#    motor_stp()
#    
#    motor_fr(280)
#    time.sleep(0.5)
#    motor_stp()
#
#    motor_r_yengec(330)
#    time.sleep(2.5)
#    motor_stp()
#    
#    motor_r_yengec(330)
#    time.sleep(2.5)
#    motor_stp()
#    
#    motor_fr(280)
#    time.sleep(0.5)
#    motor_stp()
#
#    motor_r_yengec(330)
#    time.sleep(2.5)
#    motor_stp()

### birin sonu
    
#    motor_l_yengec(330)
#    time.sleep(1.25)
#    motor_stp()
#    
#    motor_l_donus(330)
#    time.sleep(1.30)
#    motor_stp()
    


### diğerinin bası

#    motor_l_yengec(330)
#    time.sleep(2.5)
#    motor_stp()
#    
#    motor_l_yengec(330)
#    time.sleep(2.5)
#    motor_stp()
    
#    motor_fr(280)
#    time.sleep(0.5)
#    motor_stp()

#    motor_l_yengec(330)
#    time.sleep(2.5)
#    motor_stp()
    
#    motor_l_yengec(330)
#    time.sleep(2.5)
#    motor_stp()
    
#    motor_fr(280)
#    time.sleep(0.5)
#    motor_stp()

#    motor_l_yengec(330)
#    time.sleep(2.5)
#    motor_stp()

# diğerinin sonu



    #motor_l_donus(330)
    #time.sleep(0.7)
    #motor_l_donus(330)
    #time.sleep(0.7)
    #motor_stp()
    
    #motor_l_yengec(330)
    #time.sleep(3)
    #motor_stp()

    #motor_r_donus(345)
    #time.sleep(0.4)
    #motor_stp()
    
    x = int(input("Enter x: "))
    #y = int(input("Enter y: "))
    

#motor_fr(270)
#time.sleep(5)

#motor_ud(340)
#time.sleep(4)

#motor_ud(340)
#time.sleep(4)

#
# motor_r_donus(340)
# time.sleep(1)
#
# motor_l_donus(340)
# time.sleep(1)
#
#motor_l_yengec(340)
#time.sleep(4)
#
#motor_r_yengec(340)
#time.sleep(4)

#ilk_deneme()
#motor_stp()
#arama_deneme()

motor_stp()
time.sleep(1)
GPIO.output(S_GPIO, GPIO.LOW)
print("deneme bitti")