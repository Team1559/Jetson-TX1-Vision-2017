import cv2
import numpy as np


#some values
hsvl = np.array((60,30,200));
hsvh = np.array((90,255,255));
minarea = 10
maxarea = 200
found = True


#pop some caps
cap = cv2.VideoCapture(0)

#values to find average of two centroids
cx = 0
cy = 0

while 1:
	#grab some frames
	_,frame = cap.read()

	cx = cy = 0

	#convert to hsv
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	thresh = cv2.inRange(hsv, hsvl, hsvh)
	threshcp = thresh.copy()

	#find some contours
	contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

	#grab the two biggest areas
	contours = sorted(contours, key=cv2.contourArea, reverse = True)[:2]

	#find centroids of contours
	i = 0
	for cnt in contours:

		if cv2.contourArea(cnt) < minarea:
			cx = cy = -1
			found = False
			print "false"
			break;

		print cv2.contourArea(cnt)

		#if cv2.contourArea(cnt) > maxarea:
			#cx = cy = -1
                        #found = False
                        #print "false"
                        #break;


		#M = cv2.moments(cnt)
		#x,y = int(M['m10']/M['m00']), int(M['m01'],M['m00'])

		#if i == 0:
		#	cnt1 = cnt
		#elif i == 1:
		#	cnt2 = cnt
		#i+=1

	#if found:
		M1 = cv2.moments(cnt)
		#M2 = cv2.moments(cnt2)
		#print "here"
		hull_cnt = cv2.convexHull(cnt)
		#hull_cnt2 = cv2.convexHull(cnt2)
		x1,y1 = int(M1['m10']/M1['m00']), int(M1['m01']/M1['m00'])
		#x2,y2 = int(M2['m10']/M2['m00']), int(M2['m01']/M2['m00'])
		#cx = (x1+x2)/2
		#cy = (y1+y2)/2

		cx += x1
		cy += y1

		print cx," ",cy

		#draw it
		#cv2.drawContours(frame, hull_cnt1, -1 (0,255,0), 3)
		#cv2.drawContours(frame, hull_cnt2, -1 (0,255,0), 3)
		#cv2.circle(frame,(cx,cy),5,255,-1)

		#found = False

	cx = cx/2
	cy = cy/2

	#draw it
	if found:
		#print "ay"
        	#cv2.drawContours(frame, hull_cnt, -1 (0,255,0), 3)
        	#cv2.drawContours(frame, hull_cnt2, -1 (0,255,0), 3)
        	cv2.circle(frame,(cx,cy),5,255,-1)
	found = True

	#show the image
	cv2.imshow("thresh", threshcp)
	cv2.imshow("frame", frame)
	cv2.waitKey(1)
