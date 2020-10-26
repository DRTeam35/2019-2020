# image processing lib.
import cv2
import numpy as np
import time

j=1

def control(center, circle):  # ekranın merkezi ile çemberin merkezini kıyaslama
    x = center[0] - circle[0]
    y = center[1] - circle[1]
    return x, y

def konumlama(center, circle):
    dif = control(center, circle)  # x, y
    if dif[0] <= 0 and dif[1] > 0:  # 1. region
        print("Hedef 1. bolgede")
        # araç t sn sağa gidecek
        print("saga gidiliyor...")
        print("yukarı gidiliyor...")

    elif dif[0] > 0 and dif[1] > 0:  # 2. region
        print("Hedef 2. bolgede")
        # araç t sn sola gidecek
        print("sola gidiliyor...")
        # araç t sn yukarı gidecek
        print("yukarı gidiliyor...")

    elif dif[0] >= 0 and dif[1] <= 0:  # 3. region
        print("Hedef 3. bolgede")
        # araç t sn sola gidecek
        print("sola gidiliyor...")
        print("asagı gidiliyor...")

    elif dif[0] < 0 and dif[1] <= 0:  # 4. region
        print("Hedef 4. bolgede")
        # araç t sn sağa gidecek
        print("saga gidilecek...")
        print("asagı gidiliyor...")

    else:
        print("Osman, problemimiz var!")


def gudumleme(yari_cap, thr):  # ekrandaki çemberin yarı çapını al, threshold değer ile karşılaştır, duruma göre güdümle
    print("gudumleme fonksiyonuna girildi!")
    thr_f = thr * 0,60  # karşılaştırma için threshold değeri
    if yari_cap < thr_f:  # biraz ilerlemeye ihtiyacın va
        print("ilerliyor...")

    elif yari_cap >= thr_f:  # yeterince yakınsın, bas gaza
        print("yeeyy, mişşın kompleytıt")

    return 0

def FindCircle(img, min, max,j):

    print("FindCirc calısıyor...")
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.medianBlur(img_gray, 7)
    cv2.imshow("img", img)
    cv2.imwrite('/home/fece/DEU ROV/images/img_image%s.jpg' %j, img)
    print("img cekti")
    kernal = np.ones((1, 1), "uint8")
    img = cv2.dilate(img_blur, kernal)
    cv2.imshow("filtered image", img)

    circle = cv2.HoughCircles(img_gray, cv2.HOUGH_GRADIENT, 1, img.shape[0] / 64,
                              param1=30, param2=20,
                              minRadius=min, maxRadius=max)
    if circle is None:
        ######################## Arama Fonksiyonu############
        #arama_deneme()
        print("arama calısacak!!!!!!")
        print("circle yok")
        return(FindCircle(frame,0,200,j))


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
        print(circle)
        cv2.imshow("detected", img)
        cv2.imwrite('/home/fece/DEU ROV/images/image%s.jpg' % j,img)
        print("detecected cekildi")
        j += j # save the "img" as 'submarine1_2.png'
        # "img"'yi 'submarine1_2.png' olarak kaydet
        return circle,j

    else:
        print("gecmis olsun")
        return 0
    cv2.destroyAllWindows()

cap = cv2.VideoCapture(0)
#cap = cv2.resize(cap,(720,480))
j=1

while cap.isOpened():
    # Capture frame-by-frame
    _, frame = cap.read()
    frame = cv2.flip(frame,0)
    frame = cv2.flip(frame,1)
    dimensions = frame.shape
    height = frame.shape[0]
    width = frame.shape[1]
    center = (width / 2, height / 2)  # 360, 240
    center = np.int0(center)
    print("screen center = {}".format(center))

    circle,j = FindCircle(frame, 0, 200,j)
    time.sleep(3)

    if center[0] in range(circle[0] - 25, circle[0] + 25) \
            and center[1] in range(circle[1] - 25, circle[1] + 25):
        #################### Güdümleme
        print("Güdümleme")
        gudumleme(circle[2],center[0])
        # çember boyut sınırlama ve bitiş
        # mission tamamlandı, yukarı çıkabilirsin
        cap.release()
        cap = cv2.VideoCapture(0)

    else:
        ################### Konumlama
        print("Konumlama")
        # x ekseninde konumlan
        konumlama(center,circle)
        ###FindCircle(img, circle[2] - 5, circle[2] + 5)
        cap.release()
        cap = cv2.VideoCapture(0)


        # y ekseninde konumlan
    if cv2.waitKey(50) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
