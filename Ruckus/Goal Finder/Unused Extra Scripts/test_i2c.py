import i2c

i2c.startServer()


while True:

	i2c.putData(80.12)
