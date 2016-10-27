#!/usr/bin/python

import cv2
import numpy as np
import time
import logging
logging.basicConfig(level=logging.DEBUG)
#import serialserver
import sys
import math
import angle
import distance
import gripejuicer
#import i2c
#import timer
import v4l2capture
import select



#read the USB drive
try:
	r = gripejuicer.Reader()
	lowValue = r.getLowValue()
	highValue = r.getHighValue()
	brightness = r.getBrightness()
except (IOError, IndexError, ValueError):
	print "No drive found, using standard values"
	lowValue = np.array((60,120,10))
	highValue = np.array((100,255,255))
	brightness = 0.0
	#lowValue = np.array((70,120,10))
	#highValue = np.array((120,255,255))


print lowValue
print highValue
print brightness


#user supplied argument to display image
showImage = False

for arg in sys.argv:
    if arg == 'y':
        showImage = True
    elif arg.startswith("?"):
        print 'y: show image \n n: do not show image \n if blank: does not show image'
    else:
        print 'unknown: "%s"' % arg


#log errors
sys.stderr.write("Image Processing Working\n")


#create camera variables
width = 800
height = 480


#create video capture
cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cap.set(cv2.CAP_PROP_BRIGHTNESS, brightness)
#cap = v4l2capture.Video_device("/dev/video1")
#cap.create_buffers(30)
#cap.queue_all_buffers()
#cap.start()


#create some variables
cx = 0 #centroid x
cy = 0 #centroid y
minxyratio = 10000
maxxyratio = -10000


#create data to be sent
global error
global dist
global ang
error = 0
dist = 0.0
ang = 0.0


#start a timer for recording fps
#fpscounter = timer.Timer()


#open the serial server
#serialserver.startServer()


#open the i2c channel
#i2c.startServer()


while(1):

    #read the frames
    #select.select((cap,), (), ())
    #data = cap.read_and_queue()
    #frame = cv2.imdecode(np.frombuffer(data, dtype=np.uint8), cv2.IMREAD_COLOR)

    _,frame = cap.read()


    #for calibration
    #cv2.imwrite("calibrate.png", frame)

    #convert to hsv and find range of colors
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    thresh = cv2.inRange(hsv, lowValue, highValue)
    thresh2 = thresh.copy()

    #blur it
    thresh = cv2.blur(thresh, (5,5))

    #erode and dilate
    thresh = cv2.erode(thresh, (3,3))
    thresh = cv2.dilate(thresh, (3,3))

    #find contours in the threshold image
    _, contours, _ = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    # finding contour with maximum area and store it as best_cnt
    min_area = 1700
    best_cnt = None

    #sort by greatest areas
    contours = sorted(contours, key = cv2.contourArea, reverse = True)[:4]


    for cnt in contours:

        area = cv2.contourArea(cnt)
        if area < min_area:
             continue

	#filter by ratio of contour area/ bounding rectangle area
        rx,ry,rw,rh = cv2.boundingRect(cnt)
        arearatio = rw * rh / area

        #find centroids of all contours
        M = cv2.moments(cnt)
        cx,cy = int(M['m10']/M['m00']), int(M['m01']/M['m00'])

        #filter by ratios
        yratio = (cy-ry)/(rh*1.0)
        xratio = (cx-rx)/(rw*1.0)
        xyratio = yratio/xratio
        #print xyratio
        if 1.05 < xyratio < 1.34:  #low originlly at 1.14
            best_cnt = cnt
            #print "Found Shape!"
            break

        #if 1.8 < arearatio < 3.8 and area > min_area:
           #best_cnt = cnt
        #print "area:", rw*rh / area


    #check if any shape was found
    if best_cnt == None:
         cx = cy = -600 #sends a -1000 over serial
         #print "Nothing Found!"
    else:
    	#finding centroids of best_cnt and draw a circle there
    	M = cv2.moments(best_cnt)
    	hull_cnt = cv2.convexHull(best_cnt)
    	#print min_area/cv2.contourArea(hull_cnt)
    	cv2.drawContours(frame, hull_cnt, -1, (0,255,0), 3)
    	cx,cy = int(M['m10']/M['m00']), int(M['m01']/M['m00'])
    	cv2.circle(frame,(cx,cy),5,255,-1)



    #find the error
    error = cx-400

    #find the angle
    if error != -1000:
         ang = angle.getAngle(error)
    else:
        #no target found, do not calculate the angle
        ang = -1000



	#make sure there is an object before finding distance and angle
    #if (cy > -1 and cx > -1):
		#dist = distance.findDistance(cy)
		#ang = angle.getAngle(dist, error)
    #else:
		#return -1 if no object is found
		#ang = dist = -1

    #dist = 1


    #give values to server
    #serialserver.putData(ang)


    #send the values over i2c
    #i2c.putData(ang)


    #count how many frames have been processed
    #fpscounter.update()


    #show the image based on user values
    if showImage == True:
        cv2.imshow("thresh", thresh2)
        cv2.imshow("frame", frame)
        cv2.waitKey(1)


    #print for testing
    print ang
    #print cy

