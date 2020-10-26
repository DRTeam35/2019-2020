import cv2
import numpy as np

img = cv2.imread("circ3.jpeg")


#dimensions = img.shape
center = [250,250]
#center = (img.shape[0] / 2, img.shape[1] / 2)
center = np.int0(center)
print("screen center = {}".format(center))
cv2.circle(img, (center[0], center[1]), 3, (0, 0, 255), 2)


def FindCircle(img, min, max):
    
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.medianBlur(img_gray, 7)
    cv2.imshow("img", img)
    kernal = np.ones((1, 1), "uint8")
    img = cv2.dilate(img_blur, kernal)
    cv2.imshow("filtered image", img)
    circle = cv2.HoughCircles(img_gray, cv2.HOUGH_GRADIENT, 1, img.shape[0] / 60,
                              param1=30, param2=20,
                              minRadius=min, maxRadius=max)
    if circle is None:
        print("circle yok!")
    if circle is not None:
        circle = np.uint16(np.around(circle))
        # print(circle)
        # for a in circle[:]:
        #   cv2.circle(img,(circle[a][0],circle[a][1]),circle[a][2],(255,255,0),1)
    for i in circle[0, :]:
        cv2.circle(img, (i[0], i[1]), i[2], (255, 0, 0), 2)
        cv2.circle(img, (i[0], i[1]), 2, (255, 0, 0), 10)
        circle = (i[0], i[1], i[2])
        print(i[2])
        circle = np.int0(circle)
        break
    print("circle coord = {}".format(circle))
    cv2.imshow("detected", img)
    return circle


circle = FindCircle(img, 0, 500)

if center[0] in range(circle[0] - 25, circle[0] + 25) and center[1] in range(circle[1] - 25, circle[1] + 25):
    ########GÜDÜMLEME################
    print("Güdümleme")
    #########yarıcap bilgisi kıyaslama#################
else:
    #######KONUMLAMA##################
    print("Konumlama")
    """
    img2 = cv2.imread("circ1.jpeg")
    FindCircle(img2, circle[2] - 50, circle[2] + 50)
    """

cv2.waitKey(0)
cv2.destroyAllWindows()