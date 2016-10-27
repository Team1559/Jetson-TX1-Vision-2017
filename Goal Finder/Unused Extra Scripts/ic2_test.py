#!usr/bin/python

import smbus

address = 0x05

bus = smbus.SMBus(1)
bus.write_byte_data(address, ord("s"), 0)

