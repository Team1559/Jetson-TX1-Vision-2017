import numpy as np
import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 15559
#host = "10.15.59.6"
x = 0
y = 0


def setup(self):
	s.bind((host,port))


def accept(self):
	s.listen(5)
	c, ref = s.accept()


def send(x, y):
	c.send(x)
	c.send(y)


def close(self):
	c.close()
	sys.exit()
	


