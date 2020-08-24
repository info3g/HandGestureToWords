import cv2
import numpy as np


cap = cv2.VideoCapture(0)

while True:
	ret,frame = cap.read()

	im_ycrcb = cv2.cvtColor(frame,cv2.COLOR_BGR2YCR_CB)
	cv2.rectangle(frame,(0,0),(200,200),(255,0,0),2)
	roi = frame[0:200,0:200]
	roi = cv2.cvtColor(roi,cv2.COLOR_BGR2YCR_CB)
	#detect skin color
	skin_yrcrb_mint = np.array([0,133,77],np.uint8)
	skin_yrcrb_maxt = np.array([255,173,127],np.uint8)
	
	skin_ycrcb = cv2.inRange(roi,skin_yrcrb_mint,skin_yrcrb_maxt)
	skin_ycrcb = cv2.blur(skin_ycrcb,(7,7)) 
	
	cv2.imshow('skin_ycrcb',skin_ycrcb)
	cv2.imshow('frame',frame)


	c=cv2.waitKey(1)
	if c==27:
		break
	
