import cv2
import numpy as np

src = cv2.imread('Sample Image.png')
src = cv2.resize(src,(512,512))

red = np.zeros((512,512),dtype=np.uint8)
green = np.zeros((512,512),dtype=np.uint8)

lower_red = np.array([230,20,30],dtype=np.uint8)
upper_red = np.array([240,30,40],dtype=np.uint8)

lower_green = np.array([30,170,70],dtype=np.uint8)
upper_green = np.array([40,180,80],dtype=np.uint8)

#src_color = src
src_color = cv2.cvtColor(src,cv2.COLOR_BGR2RGB)

threshold_red = cv2.inRange(src_color,lower_red, upper_red)
threshold_green = cv2.inRange(src_color,lower_green, upper_green)

is_red, contours_red, _ = cv2.findContours(threshold_red, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
is_green, contours_green, _ = cv2.findContours(threshold_green, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

if(len(is_red)>0):
	cv2.drawContours(red, contours_red, -1, (255, 137, 59), 1)
	print(contours_red)

if(len(is_green)>0):
	cv2.drawContours(green, contours_green, -1, (0, 137, 59), 1)
	print(contours_green)

cv2.imshow('Maze',src)
cv2.imshow('Red',red)
#cv2.imshow('Green',green)
cv2.waitKey(0)