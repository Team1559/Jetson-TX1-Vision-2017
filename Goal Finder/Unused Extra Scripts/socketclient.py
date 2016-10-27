import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 10.15.59.6
port = 15559

s.connect((host, port))
print s.recv(1024)
print s.recv(1024)
print s.recv(1024)
print s.recv(1024)
print s.recv(1024)
s.close


###BROKEN###
#def sendKill():
#	s.listen()
#	c = s.accept()
#	killCode = "true"
#	c.send(killCode)

#sendKill()
