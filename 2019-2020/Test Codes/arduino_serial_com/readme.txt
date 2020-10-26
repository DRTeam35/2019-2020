connect your arduino directly to raspberrypi usb port to get the serial communication
run your .ino code in your arduino
then, run "arduinoserial2.py", which works well

becareful about "serial.Serial('/dev/ttyUSB0', 9600)"
9600 might change depending on your .ino code, check it
ttyUSB0 is the port that is assigned by your raspberrypi, you need to check it

pi@raspberrypi $ ls /dev/ttty*
this'll show you "ttyUSB0" or smt else, just check it when arduino is connected and when arduino is not connected,
there must be some changing at the end