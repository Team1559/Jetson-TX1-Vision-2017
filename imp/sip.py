import cv2
import numpy as np

#vals
hsvlR = np.array((20,30,200))
hsvhR = np.array((90,255,255))
hsvlL = np.array((60,30,200))
hsvhL = np.array((90,255,255))

#poppin caps
caps = [cv2.VideoCapture(0), cv2.VideoCapture(1)]

#more vals
cx = [0,0]
cy = [0,0]

found = True

while 1:

	_,frameL = caps[0].read()
	_,frameR = caps[1].read()

	#for x in cx:
	#	x = 0
	#for y in cy:
	#	y = 0

	hsvL = cv2.cvtColor(frameL, cv2.COLOR_BGR2HSV)
	hsvR = cv2.cvtColor(frameR, cv2.COLOR_BGR2HSV)
	threshL = cv2.inRange(hsvL, hsvlL, hsvhL)
	threshR = cv2.inRange(hsvR, hsvlR, hsvhR)

	threshcpR = threshR.copy()
	threshcpL = threshL.copy()

        #find some contours
        contoursR, _ = cv2.findContours(threshR, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	contoursL, _ = cv2.findContours(threshL, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)


        #grab the two biggest areas
        contoursR = sorted(contoursR, key=cv2.contourArea, reverse = True)[:2]
	contoursL = sorted(contoursL, key=cv2.contourArea, reverse = True)[:2]


	for cnt in contoursR:

		if cv2.contourArea(cnt) < 15:
			cx[0] = -1
			cy[0] = -1
			found = False
			break;

		M1 = cv2.moments(cnt)
		x,y = int(M1['m10']/M1['m00']), int(M1['m01']/M1['m00'])

		cx[0] += x
		cy[0] += y

	for cnt in contoursL:

		if cv2.contourArea(cnt) < 15:
                        cx[1] = -1
			cy[1] = -1
                        found = False
                        break;

                M1 = cv2.moments(cnt)
                x,y = int(M1['m10']/M1['m00']), int(M1['m01']/M1['m00'])

                cx[1] += x
                cy[1] += y

	#for x in cx:
	#	x = x/2

	#for y in cy:
	#	y = y/2
	cx[0] = cx[0]/2
	cx[1] = cx[1]/2
	cy[0] = cy[0]/2
	cy[1] = cy[1]/2


	if found:
        	cv2.circle(frameR,(cx[0],cy[0]),5,255,-1)
		cv2.circle(frameL,(cx[1],cy[1]),5,255,-1)
          	#cv2.circle(threshcp,(cx,cy),15,120,1)
                #cv2.line(threshcp,(cx,cy-17),(cx,cy+17),150,2)
                #cv2.line(threshcp,(cx-17,cy),(cx+17,cy),150,2)
                #cv2.line(frame,(cx,0),(cx,480),70,2)
                #cv2.line(frame,(0,cy),(640,cy),70,2)
	found = True


	print "right ",cx[0]," ",cy[0]
	print "left ",cx[1]," ",cy[1]

	cv2.imshow("righthsv", threshcpR)
	cv2.imshow("lefthsv", threshcpL)
	cv2.imshow("right", frameR)
	cv2.imshow("left", frameL)
	cv2.waitKey(1)
