
import serial

port = serial.Serial("/dev/ttyAMA0", baudrate = 115200, timeout = 5.0)

while 1:
	x = port.read()
	print x

