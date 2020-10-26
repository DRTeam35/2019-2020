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
servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)  # high/low of gpio
GPIO.output(servoPIN, GPIO.HIGH)

j = 1  # to save frame and detected images

def motor_fr(p):  # ileri/geri motorlar
    pwm.set_pwm(4, 0, p)
    pwm.set_pwm(5, 0, p)
    pwm.set_pwm(6, 0, p)
    pwm.set_pwm(7, 0, p)


def motor_ud(p):  # yukarı/aşağı motorlar
    pwm.set_pwm(0, 0, p)
    pwm.set_pwm(1, 0, p)
    pwm.set_pwm(2, 0, p)
    pwm.set_pwm(3, 0, p)


def motor_r_yengec(p):  # sağ/sol motorlar
    #################################
    fark = p - 311
    pwm2 = 311 - fark
    pwm.set_pwm(4, 0, pwm2-0)
    pwm.set_pwm(5, 0, p+0)
    pwm.set_pwm(6, 0, p+10)
    pwm.set_pwm(7, 0, pwm2-10)


def motor_l_yengec(p):  # sağ/sol motorlar
    #################################
    fark = p - 311
    pwm2 = 311 - fark
    pwm.set_pwm(4, 0, p+0)
    pwm.set_pwm(5, 0, pwm2-0)
    pwm.set_pwm(6, 0, pwm2-10)
    pwm.set_pwm(7, 0, p+10)


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


def motor_stp():  # motorları durdur
    pwm.set_pwm(0, 0, 309)  # sağ ön dikey
    pwm.set_pwm(1, 0, 309)  # sol ön dikey
    pwm.set_pwm(2, 0, 309)  # sağ arka dikey
    pwm.set_pwm(3, 0, 309)  # sol arka dikey
    pwm.set_pwm(4, 0, 311)  # sağ ön itici
    pwm.set_pwm(5, 0, 311)  # sol ön itici
    pwm.set_pwm(6, 0, 310)  # sağ arka itici
    pwm.set_pwm(7, 0, 311)  # sol arka itici
    time.sleep(0.75)


def control(center, circle):  # ekranın merkezi ile çemberin merkezini kıyaslama
    x = center[0] - circle[0]
    y = center[1] - circle[1]
    return x, y


def konumlama(center, circle):

    dif = control(center, circle)  # x, y

    r_pwm = 330  # aracın sağa gidiş pwm i
    r_t = 2  # aracın sağa gidiş süresi

    u_pwm = 330  # aracın yukarı çıkış pwm i
    u_t = 0.75  # aracın yukarı çıkış süresi

    l_pwm = 330  # aracın sola gidiş pwm i
    l_t = 2  # aracın sola gidiş süresi

    d_pwm = 290  # aracın aşağı gidiş pwm i
    d_t = 0.75  # aracın aşağı gidiş süresi

    if dif[0] <= 0 and dif[1] > 0:  # 1. region
        print("Hedef 1. bolgede")
        # araç t sn sağa gidecek
        
     
        print("saga gidiliyor...")
        motor_r_yengec(r_pwm)
        time.sleep(r_t)
        motor_l_yengec(r_pwm)
        time.sleep(1)
        motor_stp()
      
        
        
        # araç t sn yukarı gidecek
        print("yukarı gidiliyor...")
        motor_ud(u_pwm)
        time.sleep(u_t)
        motor_stp()


    elif dif[0] > 0 and dif[1] > 0:  # 2. region
        print("Hedef 2. bolgede")
        # araç t sn sola gidecek
        print("sola gidiliyor...")
        
        motor_l_yengec(l_pwm)
        time.sleep(l_t)
        motor_r_yengec(r_pwm)
        time.sleep(1)
        motor_stp()
       
        
        # araç t sn yukarı gidecek
        print("yukarı gidiliyor...")
        motor_ud(u_pwm)
        time.sleep(u_t)
        motor_stp()

    elif dif[0] >= 0 and dif[1] <= 0:  # 3. region
        print("Hedef 3. bolgede")
        # araç t sn sola gidecek
        print("sola gidiliyor...")
        
        motor_l_yengec(l_pwm)
        time.sleep(l_t)
        motor_r_yengec(r_pwm)
        time.sleep(1)
        motor_stp()
        
        # araç t sn aşağı gidecek
        print("asagı gidiliyor...")
        motor_ud(d_pwm)
        time.sleep(d_t)
        motor_stp()

    elif dif[0] < 0 and dif[1] <= 0:  # 4. region
        print("Hedef 4. bolgede")
        # araç t sn sağa gidecek
        print("saga gidilecek...")
      
        motor_r_yengec(r_pwm)
        time.sleep(r_t)
        motor_l_yengec(r_pwm)
        time.sleep(1)
        motor_stp()
       
        # araç t sn aşağı gidecek
        print("asagı gidiliyor...")
        motor_ud(d_pwm)
        time.sleep(d_t)
        motor_stp()

    else:
        print("Osman, problemimiz var!")


def gudumleme(yari_cap, thr):  # ekrandaki çemberin yarı çapını al, threshold değer ile karşılaştır, duruma göre güdümle
    print("gudumleme fonksiyonuna girildi!")
    thr = int(thr) # to handle the tuple problem
    thr_f = round(thr * 0,65)  # karşılaştırma için threshold değeri
    a = 5

    if yari_cap < thr_f:  # biraz ilerlemeye ihtiyacın var
        motor_fr(340)
        time.sleep(3)
        motor_stp()
        print("ilerliyor...")


    # elif yari_cap >= thr_f:  # yeterince yakınsın, bas gaza
    else:
        motor_fr(340)
        time.sleep(4)
        motor_stp()
        #motor_ud(340)
        #time.sleep(2)
        #motor_stp()
        print("yeeyy, mişşın kompleytıt")
        a = 10

    return a


def start():
    print("start calisiyor")
    motor_stp()

    motor_ud(280) # hızlı iniyor
    time.sleep(2)
    motor_stp()

########################
    #motor_l_donus(330) # arac havuzun sağından bırakıldı
    #time.sleep(2)
    #motor_stp()

    motor_r_donus(330)  # arac havuzun solundan bırakıldı
    time.sleep(2)
    motor_stp()
############################

    for i in range(0,7): # 6m gitmiş oldu, havuzu ortaladı
        motor_fr(340)
        time.sleep(3)
        motor_stp()
    
    motor_ud(280) # hızlı iniyor
    time.sleep(2)
    motor_stp()

#    for i in range(0,3): # 6m gitmiş oldu, havuzu ortaladı
#        motor_fr(340)
#        time.sleep(3)
#        motor_stp()
#    
#    motor_ud(280) # hızlı iniyor
#    time.sleep(2)
#    motor_stp()

    #motor_r_yengec(330)
    #time.sleep(3)
    #motor_stp()
    

    motor_l_yengec(330)
    time.sleep(3)
    motor_r_yengec(330)
    time.sleep(1)
    motor_stp()

    #motor_r_donus(345)
    #time.sleep(1)
    #motor_stp()

    motor_l_donus(330)
    time.sleep(2)
    motor_stp()

    motor_fr(340)
    time.sleep(3)
    motor_stp()
    
    motor_ud(280) # hızlı iniyor
    time.sleep(2)
    motor_stp()

    motor_fr(340)
    time.sleep(3)
    motor_stp()
    
    #ek yukarı
    motor_ud(340) # hızlı çıkıyor
    time.sleep(2)
    motor_stp()


    # motor_fr(340)
    # arama_time(img, 3)
    # motor_stp()
    # # 90 derece sağa dönüş
    # motor_r_donus(330)
    # arama_time(img, 2)
    # motor_stp()
    #
    # # 1 saniye ileri
    # motor_fr(330)
    # arama_time(img, 2)
    # motor_stp()
    #
    # # 90 derece sağa dönüş
    # motor_r_donus(330)
    # arama_time(img, 2)
    # motor_stp()
    #
    # # 3 (r_t) saniye ileri
    # motor_fr(340)
    # arama_time(img, 5)
    # motor_stp()
    #
    # # 90 derece sağa dönüş
    # motor_r_donus(330)
    # arama_time(img, 2)
    # motor_stp()
    #
    # # 2 saniiye ileri
    # motor_fr(340)
    # arama_time(img, 5)
    # motor_stp()
    #
    # # 90 derece sağa dönüş
    # motor_r_donus(330)
    # arama_time(img, 2)
    # motor_stp()
    #
    # # 3 (r_t) saniye ileri
    # motor_fr(340)
    # arama_time(img, 3)
    # motor_stp()

    # bulamadı yukarı çık


def FindCircle(img, min, max):
    print("FindCirc calısıyor...")

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.medianBlur(img_gray, 1)
    #cv2.imshow("img", img)
    #cv2.imwrite('/home/pi/Desktop/DEU-ROV/images/img_image%s.jpg' % j, img)
    #print("img cekti")
    kernal = np.ones((1, 1), "uint8")
    img = cv2.dilate(img_blur, kernal)
    #cv2.imshow("filtered image", img)

    # circle detection parameters
    circle = cv2.HoughCircles(img_gray, cv2.HOUGH_GRADIENT, 1, img.shape[0] / 60,
                              param1=30, param2=20,
                              minRadius=min, maxRadius=max)
    if circle is None:
        ######################## Arama Fonksiyonu############
        #arama_deneme()
        print("arama calısacak!!!!!!")
        print("circle yok")

        return None

    elif circle is not None:
        circle = np.uint16(np.around(circle))
        # (contours, hierarchy) = cv2.findContours(img_gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        # for pic, contour in enumerate(contours):
        # area = cv2.contourArea(contour)
        i = circle[0, 0]
        cv2.circle(img, (i[0], i[1]), i[2], (255, 0, 0), 2)  # tespit edilen çemberi çiz
        cv2.circle(img, (i[0], i[1]), 2, (255, 0, 0), 10)  # tespit edilen çemberin ortasını çiz
        circle = (i[0], i[1], i[2])  # x, y, r

        circle = np.int0(circle)
        #r = int(i[2])

        print(circle)
        cv2.imshow("detected", img)
        # cv2.imwrite('/home/pi/Desktop/DEU-ROV/images/image%s.jpg' % j, img)
        # print("detecected cekildi")
        # j += j

        return circle

    else:
        print("gecmis olsun")
        return 0
    cv2.destroyAllWindows()


# def arama_time(img, t):
#     for i in range(t):
#         time.sleep(1)
#         FindCircle(img, 0, 200)


# motor initialization
#motor_stp()
pwm.set_pwm(0, 0, 311)  # sağ ön dikey
pwm.set_pwm(1, 0, 311)  # sol ön dikey
pwm.set_pwm(2, 0, 311)  # sağ arka dikey
pwm.set_pwm(3, 0, 311)  # sol arka dikey
pwm.set_pwm(4, 0, 311)  # sağ ön itici
pwm.set_pwm(5, 0, 311)  # sol ön itici
pwm.set_pwm(6, 0, 310)  # sağ arka itici
pwm.set_pwm(7, 0, 311)  # sol arka itici

time.sleep(4)
# pwm.set_pwm(channel_number, pwm_high_start, pwm_high_stop)

cap = cv2.VideoCapture(0)
# cap = cv2.resize(cap,(720,480))

m = 1 # counter to save each frame to Desktop
j = 1 # tüm havuzu tavaf etme counterı
a = 5 # gudumleme cıkıs için

motor_ud(280) # hızlı iniyor
time.sleep(2)
motor_stp()
motor_fr(330)
time.sleep(3)
motor_stp()
start()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    frame = cv2.flip(frame,0)
    frame = cv2.flip(frame,1)
    dimensions = frame.shape
    height = frame.shape[0]
    width = frame.shape[1]
    center = (width / 2, height / 2)  # 360, 240
    center = np.int0(center)
    print("screen center = {}".format(center))
    #cv2.imwrite('/home/pi/Desktop/image%s.jpg' % m, frame)

    m += 1
    circle = FindCircle(frame, 0, 200)

    if circle is None:
        motor_fr(340)
        time.sleep(2)
        motor_stp()
        motor_ud(280)
        time.sleep(2)
        motor_stp()
        j += 1

        if j == 30:
            motor_l_donus(330)
            time.sleep(4)
            motor_stp()
            j = 1

        if cv2.waitKey(50) & 0xFF == ord('q'):
            motor_stp()
            break

    elif center[0] in range(circle[0] - 60, circle[0] + 60) \
            and center[1] in range(circle[1] - 60, circle[1] + 60):
        motor_ud(280)
        time.sleep(0.5)
        motor_stp()
        #################### Güdümleme
        print("Güdümleme")
        a = gudumleme(circle[2], center[0]) # circle 2 is the radius, center 0 is the width of the screen

        cap.release()
        cap = cv2.VideoCapture(0)

        if cv2.waitKey(50) & 0xFF == ord('q'):
            motor_stp()
            break

        #break

        # çember boyut sınırlama ve bitiş
        # mission tamamlandı, yukarı çıkabilirsin
    else:
        ################### Konumlama
        print("Konumlama")
        # x ekseninde konumlan
        ####motor_ud(280)
        ####time.sleep(0.75)
        ####motor_stp()
        
              
        konumlama(center, circle)
        ###FindCircle(img, circle[2] - 5, circle[2] + 5)
        motor_fr(330)
        time.sleep(1.75)
        motor_stp()
        
        
        cap.release()
        cap = cv2.VideoCapture(0)

        if cv2.waitKey(50) & 0xFF == ord('q'):
            motor_stp()
            break

#    if a == 10:
#        motor_stp()
#        break

    if cv2.waitKey(50) & 0xFF == ord('q'):
        motor_stp()
        break

# When everything done, release the capture
GPIO.output(servoPIN, GPIO.LOW)
cap.release()
cv2.destroyAllWindows()
