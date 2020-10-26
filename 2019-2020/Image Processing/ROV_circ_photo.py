#image processing lib.
import cv2
import numpy as np
#motor control lib.
import time
import Adafruit_PCA9685
#switching lib.
from time import sleep
import RPi.GPIO as GPIO

#from picamera import PiCamera

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50) #freq of the motors 50/60 Hz

#power switching on/off
servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT) # DÜŞÜNNNN!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! high/low of gpio

#motor initialization
motor_stp()

#pwm.set_pwm(channel_number, pwm_high_start, pwm_high_stop)

img = cv2.imread("circ1.jpg")
img = cv2.resize(img, (720, 480))

dimensions = img.shape
height = img.shape[0]
width = img.shape[1]
center = (width/2, height/2) # 360, 240
center=np.int0(center)
print("screen center = {}".format(center))
cv2.circle(img, (center[0],center[1]),3, (0, 0, 255), 2)

def FindCircle (img,min,max):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.medianBlur(img_gray, 7)
    cv2.imshow("img", img)
    kernal = np.ones((1, 1), "uint8")
    img = cv2.dilate(img_blur, kernal)
    cv2.imshow("filtered image", img)
    circle = cv2.HoughCircles(img_gray,cv2.HOUGH_GRADIENT,1,img.shape[0]/60,
                              param1=30, param2=20,
                              minRadius=min, maxRadius=max)
    if circle is None:
        ######################## Arama Fonksitonu
        print("circle yok")
        Arama()

    if circle is not None:
        circle = np.uint16(np.around(circle))
        # (contours, hierarchy) = cv2.findContours(img_gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        # for pic, contour in enumerate(contours):
        # area = cv2.contourArea(contour)
        i = circle[0,0]
        cv2.circle(img, (i[0], i[1]), i[2], (255, 0, 0), 2)  # tespit edilen çemberi çiz
        cv2.circle(img, (i[0], i[1]), 2, (255, 0, 0), 10)  # tespit edilen çemberin ortasını çiz
        circle = (i[0], i[1], i[2]) # x, y, r
        circle = np.int0(circle)

    print(circle)
    cv2.imshow("detected", img)
    return circle

circle = FindCircle(img,100,200)

if center[0] in range(circle[0] - 25, circle[0] + 25) and center[1] in range(circle[1] - 25, circle[1] + 25):
    #################### Güdümleme
    print("Güdümleme")
    gudumleme(circle[2])
    #çember boyut sınırlama ve bitiş
    #mission tamamlandı, yukarı çıkabilirsin
else:
    ################### Konumlama
    print("Konumlama")
    konumlama(center, circle)
    ###FindCircle(img, circle[2] - 5, circle[2] + 5)

cv2.waitKey(0)
cv2.destroyAllWindows()

def Arama(): # çember arama algoritması
    ###################################

def control(center, circle): # ekranın merkezi ile çemberin merkezini kıyaslama
    x = center[0]-circle[0]
    y = center[1]-circle[1]
    return x,y

def konumlama(center, circle):
    dif = control(center, circle) # x, y
    r_pwm = ... # aracın sağa gidiş pwm i
    r_t = ... # aracın sağa gidiş süresi
    u_pwm = ... # aracın yukarı çıkış pwm i
    u_t = ... # aracın yukarı çıkış süresi
    l_pwm = ... #aracın sola gidiş pwm i
    l_t = ... # aracın sola gidiş süresi
    d_pwm = ... #aracın aşağı gidiş pwm i
    d_t = ... #aracın aşağı gidiş süresi

    if dif[0]<=0 and dif[1]>0: # 1. region
        # araç t sn sağa gidecek
        motor_rl(r_pwm)
        time.sleep(r_t)
        motor_stp()
        # araç t sn yukarı gidecek
        motor_ud(u_pwm)
        time.sleep(u_t)
        motor_stp()
        
    elif dif[0]>0 and dif[1]>0: # 2. region
        # araç t sn sola gidecek
        motor_rl(l_pwm)
        time.sleep(l_t)
        motor_stp()
        # araç t sn yukarı gidecek
        motor_ud(u_pwm)
        time.sleep(u_t)
        motor_stp()

    elif dif[0]>=0 and dif[1]<=0: # 3. region
        # araç t sn sola gidecek
        motor_rl(l_pwm)
        time.sleep(l_t)
        motor_stp()
        # araç t sn aşağı gidecek
        motor_ud(d_pwm)
        time.sleep(d_t)
        motor_stp()

    elif dif[0]<0 and dif[1]<=0: # 4. region
        # araç t sn sağa gidecek
        motor_rl(r_pwm)
        time.sleep(r_t)
        motor_stp()
        # araç t sn aşağı gidecek
        motor_ud(d_pwm)
        time.sleep(d_t)
        motor_stp()
    else:
        print("Osman, problemimiz var!")

def gudumleme(yari_cap): # ekrandaki çemberin yarı çapını al, threshold değer ile karşılaştır, duruma göre güdümle
    thr = ... # karşılaştırma için threshold değeri
    f_pwm = ... # motorun ileri gitmesi için verilecek olan pwm değeri
                # ileri -> <320-375>
                # geri -> <300-245>
    v_pwm = ... # aracın su üstüne çıkışı için verilecek olan pwm değeri
    v_t = ... # motorların yukarı çıkış süresi
    f_t = ... # motorların ileri çalışma süresi
    f_t2 = ... # motorların çemberi geçerken çalışma süresi
    if yari_cap < thr: # biraz ilerlemeye ihtiyacın var
        motor_fr(f_pwm)
        time.sleep(f_t)
        motor_stp()
    elif yari_cap >= thr: # yeterince yakınsın, bas gaza 
        motor_fr(f_pwm)
        time.sleep(f_t2)
        motor_stp()
        motor_ud(v_pwm)
        time.sleep(v_t)
        motor_stp()
        print("yeeyy, mişşın kompleytıt")
        break


def motor_fr(pwm): # ileri/geri motorlar
    pwm.set_pwm(4, 0, pwm)
    pwm.set_pwm(5, 0, pwm)
    pwm.set_pwm(6, 0, pwm)
    pwm.set_pwm(7, 0, pwm)

def motor_ud(pwm): # yukarı/aşağı motorlar
    pwm.set_pwm(0, 0, pwm)
    pwm.set_pwm(1, 0, pwm)
    pwm.set_pwm(2, 0, pwm)
    pwm.set_pwm(3, 0, pwm)

def motor_rl(pwm): # sağ/sol motorlar
    #################################
    pwm.set_pwm(4, 0, pwm)
    pwm.set_pwm(5, 0, pwm)
    pwm.set_pwm(6, 0, pwm)
    pwm.set_pwm(7, 0, pwm)

def motor_stp(): # motorları durdur
    pwm.set_pwm(0, 0, 311) # sağ ön dikey
    pwm.set_pwm(1, 0, 311) # sol ön dikey
    pwm.set_pwm(2, 0, 311) # sağ arka dikey
    pwm.set_pwm(3, 0, 311) # sol arka dikey
    pwm.set_pwm(4, 0, 311) # sağ ön itici
    pwm.set_pwm(5, 0, 311) # sol ön itici
    pwm.set_pwm(6, 0, 310) # sağ arka itici
    pwm.set_pwm(7, 0, 311) # sol arka itici
    time.sleep(1)
