#!/usr/bin/python

from __future__ import division
from numpy import array
import cv2
import numpy as np
import time
import logging
logging.basicConfig(level=logging.DEBUG)
import serialserver
import sys
import math
import time
import angle
import distance


#log errors
sys.stderr.write("Image Processing Working\n")

# create video capture
cap = cv2.VideoCapture(0)
cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 480)

#create x and y values
x = 0
y = 0

#open the server
#serialserver.startServer()


while True:
	    
	 #read the frames
	_,frame = cap.read()

    #convert to hsv and find range of colors
	hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
	#image = cv2.inRange(hsv,np.array((42,16,50)), np.array((140,255,155)))
	image = cv2.inRange(hsv,np.array((68,112,89)), np.array((180,255,255)))
	image2 = image.copy()

	cv2.imshow("img", image)
	cv2.waitKey(10)

    #erode and dilate
	#image = cv2.erode(image, (2,2))
	#image = cv2.dilate(image, (2,2))

    
	#find contours
	(cnts,_) = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	#sort by shapes with the 5 largest areas
	cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:50]
	#goalCnt = None
	#cnt = array(cnts)
	#print cnts


	good = None
	for c in cnts:

		rx,ry,rw,rh = cv2.boundingRect(c)
		#ratio of h/w pf target
		ratio = 0.6
		print rh/rw

		if 0.55 < rh/rw < 0.65:
			x = rx
			y = ry
			good = c
			break

	
	if good is not None:
		cv2.drawContours(image, good, -1, (0,255,0), 3)
		cv2.imshow("img", image)
		cv2.waitKey(10)


		#peri = cv2.arcLength(c, True)
		#approx = cv2.approxPolyDP(c, 0.07 * peri, True)

		#check if we have at least 8 vertices to find the U
		#if len(approx) > 7:
			#goalCnt = approx
			#print goalCnt
	
		#find centroid
		#if goalCnt != None:
			#M = cv2.moments(goalCnt)
			#cen_cnt = cv2.convexHull(goalCnt)
			#cv2.drawContours(image, cen_cnt, -1, (0,255,0), 3)
			#x,y = int(M['m10']/M['m00']), int(M['m01']/M['m00'])
			#cv2.circle(image,(x,y),5,255,-1)
		#else:
			#set x and y to -1 if nothing is found	
			#x = y = -1
			#print "Nothing Found\n"
	
	#print x
	#find the error, distance, and angle
	error = x-320
	#make sure there is an object before finding distance and angle
	#if (y > -1 and x > -1):
		#dist = distance.findDistance(y)
		#ang = angle.getAngle(dist, error)
	#else:
		#return -1 if no object is found
	#	ang = dist = -1
	
	#print x
	#print y


	#give values to server
	#serialserver.putData(error, ang, distance)
	





#new way not work
def findGoal():
	
    #read the frames
    _,frame = cap.read()

    #convert to hsv and find range of colors
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    thresh = cv2.inRange(hsv,np.array((66,64,233)), np.array((92,255,255)))
    thresh2 = thresh.copy()

    #erode and dilate
    thresh = cv2.erode(thresh, (2,2))
    thresh = cv2.dilate(thresh, (2,2))


    (cnts, _) = cv2.findContours(frame(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:10]

	
	#filter by area
    min_area = 2000
    best_cnt = None
    #max_area = 4000

    for i, cnt in enumerate(contours):
        if i > 100:
            break
        area = cv2.contourArea(cnt)
        if area > min_area:
            min_area = area
            goalCnt = cnt

    if goalCnt == None:
         cx = cy = -1
         print "Nothing Found"
    else:
	
	    #filter by number of vertices
        for c in cnts:
		
            perimeter = cv2.arcLength(c, True)
            #change 0.02 for precision value
            approx = cv2.approxPolyDP(c, 0.02 * perimeter, True)

            #check if shape has 8 vertices
            if len(approx) == 8:
                goalCnt == approx
                break


	        #find the centroid
            moment = cv2.moments(goal_cnt)
            hull_cnt = cv2.convexHull(goal_cnt)

            #set x and y and draw on frame
        cv2.drawContours(thresh, hull_cnt, -1, (0,255,0), 3)
        cx,cy = int(M['m10']/M['m00']), int(M['m01']/M['m00'])
        cv2.circle(thresh,(cx,cy),5,255,-1)
		

		#show the final processed image
        cv2.imshow("contours", thresh)
        cv2.waitKey(5)


def Work():
	
    #read the frames
    _,frame = cap.read()

    #convert to hsv and find range of colors
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    thresh = cv2.inRange(hsv,np.array((66,64,233)), np.array((92,255,255)))
    thresh2 = thresh.copy()

    #erode and dilate
    thresh = cv2.erode(thresh, (2,2))
    thresh = cv2.dilate(thresh, (2,2))

    # find contours in the threshold image
    contours,hierarchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

    # finding contour with maximum area and store it as best_cnt
    min_area = 2000
    best_cnt = None
    #max_area = 4000

    for i, cnt in enumerate(contours):
        if i > 100:
            break
        area = cv2.contourArea(cnt)
        if area > min_area:
            min_area = area
            best_cnt = cnt

    if best_cnt == None:
         cx = cy = -1
         print "Nothing Found"
    else:
    	#finding centroids of best_cnt and draw a circle there
    	M = cv2.moments(best_cnt)
    	hull_cnt = cv2.convexHull(best_cnt)
    	#print min_area/cv2.contourArea(hull_cnt)
    	cv2.drawContours(frame, hull_cnt, -1, (0,255,0), 3)
    	cx,cy = int(M['m10']/M['m00']), int(M['m01']/M['m00'])
    	cv2.circle(frame,(cx,cy),5,255,-1)


        #show the image
        #cv2.imshow("img", frame)
        cv2.waitKey(5)

def broke():
     #read the frames
    _,frame = cap.read()

    #convert to hsv and find range of colors
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    thresh = cv2.inRange(hsv,np.array((66,64,233)), np.array((92,255,255)))
    thresh2 = thresh.copy()

    #erode and dilate
    thresh = cv2.erode(thresh, (2,2))
    thresh = cv2.dilate(thresh, (2,2))


    (cnts, _) = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:10]
    goalCnt = None


    #filter by area
    min_area = 2000
    best_cnt = None
    #max_area = 4000

    for i, cnt in enumerate(cnts):
        if i > 100:
            break
        area = cv2.contourArea(cnt)
        if area > min_area:
            min_area = area
            goalCnt = cnt

    if goalCnt == None:
         cx = cy = -1
         print "Nothing Found"
		

    #filter by number of vertices
    for c in cnts:
		
        perimeter = cv2.arcLength(c, True)
        #change 0.02 for precision value
        approx = cv2.approxPolyDP(c, 0.02 * perimeter, True)

        #check if shape has 8 vertices
        if len(approx) > 8:
            goalCnt == approx
            break

	    	#find the centroid
            moment = cv2.moments(goalCnt)
            hull_cnt = cv2.convexHull(goalCnt)

            #set x and y and draw on frame
            cv2.drawContours(thresh, hull_cnt, -1, (0,255,0), 3)
            cx,cy = int(M['m10']/M['m00']), int(M['m01']/M['m00'])
            cv2.circle(thresh,(cx,cy),5,255,-1)
        
		

    #show the final processed image
    cv2.imshow("contours", frame)
	


	#find the error, distance, and angle
    error = cx-320
	#make sure there is an object before finding distance and angle
    if (cy > -1 and cx > -1):
		dist = distance.findDistance(cy)
		ang = angle.getAngle(dist, error)
    else:
		#return -1 if no object is found
		ang = dist = -1


	#give values to server
    serialserver.putData(error, ang, distance)

    #print for testing
    #print cx
    print cy
    #print distance
    #print angle


#Clean up everything before leaving
server.close()
cv2.destroyAllWindows()
cap.release()

		













