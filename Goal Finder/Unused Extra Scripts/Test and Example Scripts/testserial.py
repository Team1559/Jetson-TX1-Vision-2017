
import serial
import sys
import thread


lock = thread.allocate_lock()

global cx = 0
global cy = 0


class Server(object):

	def __init__(self):
			
			global port
			port = serial.Serial("/dev/ttyAMA0", baudrate = 115200, timeout = 5.0)


	def send(self, x, y):
		
		error = x-320
		try:	
			port.write(str(error))
		except serial.error:
			pass
	

def startServer():
	thread.start_new_thread(run, ())


def run():
	s = serialserver()
	while 1:
		with lock:
			s.send(cx, cy)
		s.close()	


def putData(x, y):
	global cx, cy
	with lock:	
		cx = x
		cy = y

