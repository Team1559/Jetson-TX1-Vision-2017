
import sys
import numpy as np


class Reader(object):

	path = "/media/pi/GRIPE/config.gripe"


	def __init__(self):

		with open(self.path, "r") as self.target:
			self.read()


	def read(self):

		self.target.seek(0)
		stringlist = self.target.readlines()

		hhigh = int(stringlist[0])
		shigh = int(stringlist[1])
		vhigh = int(stringlist[2])
		hlow = int(stringlist[3])
		slow = int(stringlist[4])
		vlow = int(stringlist[5])

		self.brightness = float(stringlist[6])
		self.lowValue = np.array((hlow,slow,vlow))
		self.highValue = np.array((hhigh,shigh,vhigh))


	def getLowValue(self):
		return self.lowValue

	def getHighValue(self):
		return self.highValue

	def getBrightness(self):
		return self.brightness
