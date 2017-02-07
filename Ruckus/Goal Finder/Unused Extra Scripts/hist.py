#!/usr/bin/python

import sys
import cv2
import numpy as np
from matplotlib import pyplot as plt



#create variables
width = 640
height = 480
exposure = 0.001
brightness = -0.1

#create video capture
cap = cv2.VideoCapture(1)
#cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, width)
#cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, height)
#cap.set(cv2.cv.CV_CAP_PROP_EXPOSURE, exposure)
#cap.set(cv2.cv.CV_CAP_PROP_BRIGHTNESS, brightness)


_,frame = cap.read()
#cv2.imshow("img", frame)
#cv2.waitKey(5)
color = ('b', 'g', 'r')


#convert to hsv and find range of colors
hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
#thresh = cv2.inRange(hsv,np.array((50,0,230)), np.array((180,10,255)))


for i, col in enumerate(color):
	histr = cv2.calcHist([frame], [i], None, [256], [0,256])
	plt.plot(histr, color = col)
	plt.xlim([0,256])
plt.show()


#apply green filter
thresh = cv2.inRange(frame, np.array((0,128,0)), np.array((10,255,10)))

while True:

	cv2.imshow("frame", frame)
	cv2.imshow("thresh", thresh)
	cv2.waitKey(0)

