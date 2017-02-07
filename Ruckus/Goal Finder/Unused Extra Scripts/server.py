
import socket
import sys
import thread

host1 = "10.15.59.6"
host2 = "10.15.59.5"

port = 15559

#host1 for 1st pi, host2 for 2nd pi
host = host1


lock = thread.allocate_lock()


class Server(object):

	def __init__(self):

		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.s.setblocking(1)
		#host = socket.gethostname()
		self.s.bind((host,port))
		self.s.listen(5)


	def send(self, x, y):
		if self.c == None:
			return
		try:	
			self.c.send("%d,%d\n" % (x, y))
		except socket.error:
			pass


	def receive(self):
		if self.c == None:
			return
		try:
			r = self.c.recv(1024)
			print r
			return r
		except socket.error:
			pass


	def accept(self):
		try:
			self.c, ref = self.s.accept()
		except socket.error:
			self.c = None
	

	def close(self):
		if self.c == None:
			return
		self.c.close()
	

def startServer():
	thread.start_new_thread(run, ())


def run():
	s = Server()
	while 1:
		s.accept()
		with lock:
			s.send(cx, cy)
		s.close()	


def putData(x, y):
	global cx, cy
	with lock:	
		cx = x
		cy = y
	
	
	

