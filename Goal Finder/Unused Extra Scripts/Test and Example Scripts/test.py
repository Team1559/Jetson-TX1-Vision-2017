import serialserver

serialserver.startServer()

while 1:
	serialserver.send(1,2)
