from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.rotation = 180

camera.start_preview()
#camera.resolution=(1280, 720)
x = 311
i = 1
j = 1

while x!= 10:
    print("Video_start(5), Video_stop(6), photo(7), exit(10): ")
    x = int(input("Enter x: "))
    if x == 5:
        camera.start_recording('/home/pi/Desktop/video%s.h264' % j)
        j = j + 1
        sleep(1)
    if x == 6:
        camera.stop_recording()
        sleep(1)
    if x == 7:
        camera.capture('/home/pi/Desktop/image%s.jpg' % i)
        i = i + 1
        sleep(1)

sleep(2)
camera.stop_preview()