import imutils
from imutils.video import VideoStream
import argparse
import time
import cv2
import struct
import pickle
import socket
import time
import Adafruit_PCA9685
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM) #anahtarlama
S_GPIO=17
GPIO.setup(S_GPIO, GPIO.OUT)

HOST = '169.254.130.79'
#HOST = '169.254.179.63'
#HOST = '169.254.226.61' #koken

PORT = 20203

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST,PORT))
#connection = client_socket.makefile('wb')
print("Baglanti saglandi\n",HOST,":",PORT)

ap = argparse.ArgumentParser()
ap.add_argument("-p", "--picamera", type=int, default=-1)
args = vars(ap.parse_args())

vs = VideoStream(usePiCamera=args["picamera"] > 0).start()
time.sleep(0.2)
pwm =Adafruit_PCA9685.PCA9685()
yanal=0
dikey=0
donme=0
Guc=0
j=0
i=0
gripper_kapali=0
gripper_eksen_sayac=150
kamera_servo_sayac=0

pwm.set_pwm_freq(50)
for i in range(8):
    pwm.set_pwm(i,0,409)
kademe=25
while True:
    frame = vs.read()
    frame = cv2.flip(frame, 1) # vertical & horizontal flip
    frame = cv2.flip(frame, 0)
    #####frame = imutils.resize(frame, width=600)
    result, frame = cv2.imencode('.jpg', frame, [int(cv2.IMWRITE_JPEG_QUALITY), 90])
    data = pickle.dumps(frame, 0)
    size = len(data)
    #print(size)
    
    client_socket.sendall(struct.pack(">L", size) + data)
    axis = struct.unpack("12f", client_socket.recv(1024))
    leftxaxis = round(axis[0],3)+0.039
    leftyaxis = round(axis[1],3)+0.039
    rightyaxis = round(axis[2],3)+0.039
    rightxaxis = round(axis[3],3)+0.039
    hatx = axis[4]
    haty = axis[5]
    yuvarlak=axis[6]
    ucgen = axis[7]
    L1=axis[8]
    R1=axis[9]
    L2=axis[10]
    R2=axis[11]
    kademe_yuzde=kademe/100
    print(haty,yuvarlak)
    #client_socket.sendall(b'heyyyoo')
    yanal=100*leftyaxis*kademe_yuzde
    dikey=100*rightyaxis*kademe_yuzde
    donme=50*leftxaxis*kademe_yuzde
    kayma=100*hatx*kademe_yuzde
    yuk_kaldırma=100*rightxaxis*kademe_yuzde
    
    #-----------------------------------------------Güç aç kapa---------------------------------
    if ucgen==1 and Guc==1:
        pwm.set_pwm(0,0,311)
        pwm.set_pwm(1,0,311)
        pwm.set_pwm(2,0,311)
        pwm.set_pwm(3,0,311)
        pwm.set_pwm(4,0,311)
        pwm.set_pwm(5,0,311)
        pwm.set_pwm(6,0,311)
        pwm.set_pwm(7,0,311)
        GPIO.output(S_GPIO,GPIO.LOW)
        Guc=0
    elif ucgen==1 and Guc==0:
        GPIO.output(S_GPIO,GPIO.HIGH)
        Guc=1
    #----------------------------------------------Bitti------------------------------------
        
    if Guc==1:
        #---------------------------------------KADEME---------------------------------------
        if R1==1 and kademe!=100:
            kademe=kademe + 25
        if R2==1 and 25!=kademe:
            kademe=kademe - 25
        #-----------------------------------------Kademe Bitti--------------------------------
        
        #--------------------------------------------motor yön-------------------------------
        pwm.set_pwm(0,0,int(311-dikey+yuk_kaldırma))
        pwm.set_pwm(1,0,int(311-dikey+yuk_kaldırma))
        pwm.set_pwm(2,0,int(311-dikey))
        pwm.set_pwm(3,0,int(311-dikey))
        pwm.set_pwm(4,0,int(311-yanal-donme-kayma))
        pwm.set_pwm(5,0,int(311-yanal+kayma))
        pwm.set_pwm(6,0,int(310-yanal+kayma))
        pwm.set_pwm(7,0,int(311-yanal+donme-kayma))
        #-------------------------------------------Motor Kodu Biter---------------------------------------------------
        
       
    #----------------------------------------gripper yönlendirme ve aç kapa----------------------------------------
        if yuvarlak==1:    
             if gripper_kapali==0:
                 pwm.set_pwm(10,0,300)
                 gripper_kapali=1
             elif gripper_kapali==1:
                 pwm.set_pwm(10,0,150)
                 gripper_kapali=0
#####   # to use 2nd servo motor of gripper
#         if rightxaxis==1 and gripper_eksen_sayac<450:
#             gripper_eksen_sayac=gripper_eksen_sayac+5
#         if rightxaxis==-1 and 150<gripper_eksen_sayac:
#             gripper_eksen_sayac=gripper_eksen_sayac-5
#         pwm.set_pwm(9,0,gripper_eksen_sayac)
        #-----------------------------------------------Gripper kodu biter--------------------------------------------------
         
        #--------------------------------------------------Kamera Servo-----------------------------------------------------
        if haty==1 and kamera_servo_sayac<150:
            kamera_servo_sayac=kamera_servo_sayac+5
        if haty==-1 and 0<kamera_servo_sayac:
            kamera_servo_sayac=kamera_servo_sayac-5
        pwm.set_pwm(8,0,210+kamera_servo_sayac)
        #----------------------------------------------------Kamera servo bitti---------------------------------------------
               
cv2.destroyAllWindows()
vs.stop()               
client_socket.close()
