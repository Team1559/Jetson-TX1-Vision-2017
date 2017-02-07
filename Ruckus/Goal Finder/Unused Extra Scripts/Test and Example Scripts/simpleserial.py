
import serial
import sys
import thread


def send(x, y):

	error = x-320
	port.write(str(error))
	#port.write("%d,%d" % (x, y))
	print error
	#print x
	#print y


def startServer():

	global port
	port = serial.Serial("/dev/ttyAMA0", baudrate = 115200, timeout = 5.0)
	global cx, cy
	cx = 0
	cy = 0


def putData(x, y):
	with lock:	
		cx = x
		cy = y




