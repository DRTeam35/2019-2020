import time
import Adafruit_PCA9685
import RPi.GPIO as GPIO

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)
GPIO.setmode(GPIO.BCM)
S_GPIO = 17
GPIO.setup(S_GPIO, GPIO.OUT)

power = int(input("Power on(1) / off(0)?"))
if power == 1:
    GPIO.output(S_GPIO, GPIO.HIGH)
if power == 0:
    GPIO.output(S_GPIO, GPIO.LOW)

pwm.set_pwm(0, 0, 409)
pwm.set_pwm(1, 0, 409)
pwm.set_pwm(2, 0, 409)
pwm.set_pwm(3, 0, 409)
pwm.set_pwm(4, 0, 409)
pwm.set_pwm(5, 0, 409)
pwm.set_pwm(6, 0, 409)
pwm.set_pwm(7, 0, 409)

print("Maks verildi, dewamke, 311'i gir")
x = int(input("Enter x:"))
pwm.set_pwm(0, 0, x)
pwm.set_pwm(1, 0, x)
pwm.set_pwm(2, 0, x)
pwm.set_pwm(3, 0, x)
pwm.set_pwm(4, 0, x)
pwm.set_pwm(5, 0, x)
pwm.set_pwm(6, 0, x-1)
pwm.set_pwm(7, 0, x)

    
x = 311     #yukarı/aşağı
y = x       #ileri/geri
z = x       #sağ/sol

while True:
    c = str(input("move: "))

    if c == 'w':
        print("ileri")
        y = y + 25
        pwm.set_pwm(4, 0, y)
        pwm.set_pwm(5, 0, y)
        pwm.set_pwm(6, 0, y - 1)
        pwm.set_pwm(7, 0, y)

    elif c == 's':
        print("geri")
        y = y - 25
        pwm.set_pwm(4, 0, y)
        pwm.set_pwm(5, 0, y)
        pwm.set_pwm(6, 0, y - 1)
        pwm.set_pwm(7, 0, y)

    elif c == 'a':
        print("sol")

        if y > 311:
            z = y + 10
            f = z - 311
            pwm.set_pwm(4, 0, z)
            pwm.set_pwm(7, 0, z - 2 * f)
        elif y < 311:
             z = y - 10
             f = 311 - z
             pwm.set_pwm(4, 0, z)
             pwm.set_pwm(7, 0, z + 2 * f)
        elif y == 311:
            z = z + 10
            f = z - 311
            pwm.set_pwm(4, 0, z)
            pwm.set_pwm(7, 0, z - 2 * f)
            # pwm.set_pwm(?, 0, x)
            # pwm.set_pwm(?, 0, x)

    elif c == 'd':
        print("sağ")

        if y > 311:
            z = y - 10
            #f = z - 311
            f = 311 -z
            pwm.set_pwm(4, 0, z)
            pwm.set_pwm(7, 0, z - 2 * f)
        elif y < 311:
             z = y + 10
             f = 311 - z
             pwm.set_pwm(4, 0, z)
             pwm.set_pwm(7, 0, z + 2 * f)
        elif y == 311:
            z = z - 10
            f = 311 - z
            pwm.set_pwm(4, 0, z)
            pwm.set_pwm(7, 0, z + 2*f)
            # pwm.set_pwm(?, 0, x)
            # pwm.set_pwm(?, 0, x)

    elif c == '+':
        print("yukarı")
        x = x + 75
        pwm.set_pwm(0, 0, x)
        pwm.set_pwm(1, 0, x)
        pwm.set_pwm(2, 0, x-25)
        pwm.set_pwm(3, 0, x-25)

    elif c == '-':
        print("asagı")
        x = x - 25
        pwm.set_pwm(0, 0, x)
        pwm.set_pwm(1, 0, x)
        pwm.set_pwm(2, 0, x-10)
        pwm.set_pwm(3, 0, x-10)

    elif c == '0':
        print("sifirla")

        pwm.set_pwm(0, 0, 311)
        pwm.set_pwm(1, 0, 311)
        pwm.set_pwm(2, 0, 311)
        pwm.set_pwm(3, 0, 311)
        pwm.set_pwm(4, 0, 311)
        pwm.set_pwm(5, 0, 311)
        pwm.set_pwm(6, 0, 310)
        pwm.set_pwm(7, 0, 311)
        x = 311
        y = 311
        z = 311
    elif c == 'k':
        pwm.set_pwm(10,0,150)
    elif c == 'l':
        pwm.set_pwm(10,0,300)
    elif c == 'p':
        
        break
    else:
        continue

time.sleep(1)
GPIO.output(S_GPIO, GPIO.LOW)