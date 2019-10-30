import cv2
import numpy as np
import serial

import os
#import time

import entity
import QR
import constants as CONST

entity = entity.entity
port = "/dev/ttyACM0"
s1 = serial.Serial(port,9600)

dir_path = '/home/pi/Desktop/mazesolver-master/Images/'

agents = []
path = []
result = []
show = []
kernel = np.ones((5,5), np.uint8)
startPoint,endPoint = [],[]

filename = 'Maze3D_Test.jpg'
img = cv2.imread(os.path.join(dir_path,filename))

rows, cols, _ = img.shape

image = img
img =  cv2.blur(img,(5,5))
img = cv2.resize(img,(int(cols/CONST.h),int(rows/CONST.h)))

def definePoints(text,x,w,y,h):
	x = int(x/CONST.h)
	y = int(y/CONST.h)
	w = int(w/CONST.h)
	h = int(h/CONST.h)
	
	if(text == 'Start'):
		startPoint.append(int((x+w/2)/(CONST.w)))
		startPoint.append(int((y+h/2)/(CONST.w)))
	elif(text == 'End'):
		endPoint.append(int((x+w/2)/(CONST.w)))
		endPoint.append(int((y+h/2)/(CONST.w)))

	cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,255),-1)

data = QR.decodeQR(image)

[text1,(x1,w1),(y1,h1)] = data[0]
[text2,(x2,w2),(y2,h2)] = data[1]

print(text1,x1,w1,y1,h1)
print(text2,x2,w2,y2,h2)

definePoints(text1,x1,w1,y1,h1)
definePoints(text2,x2,w2,y2,h2)

cv2.imshow("Replacement",img)
cv2.waitKey(0)

rows, cols, _ = img.shape
stepx = int(rows/CONST.w)
stepy = int(cols/CONST.w)
print("Rows and Cols",rows,cols)
print("Stepx and Stepy",stepx,stepy)

grid = np.zeros((rows,cols),dtype=np.uint8)
zero = np.zeros((rows,cols),dtype=np.uint8)
results = np.zeros((rows,cols),dtype=np.uint8)

def collision(x,y):
    minX, minY = x*CONST.w,y*CONST.w
    for j in range(minY,minY+CONST.w):
        for i in range(minX,minX+CONST.w):
            if (gray[j,i]==0):
                return True
            else:
                return False

def creatNewAgent(x,y):
    newAgent = entity(x,y)
    if not collision(x,y):
        newAgent.fill = 255
        newAgent.isWall = False
    agents.append(newAgent)

if __name__ == '__main__':
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    _, gray = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY)
    gray = cv2.erode(gray,kernel,iterations=2)
 #   gray = cv2.dilate(gray,kernel, iterations=1)
    inverted = cv2.bitwise_not(gray)

    cv2.imshow('Grayed Image',gray)

    for j in range(stepx):
        for i in range(stepy):
            creatNewAgent(i,j)

    max_index = len(agents)
    itr = 0
    print(max_index)
    path.append(agents[startPoint[0]+int(startPoint[1]*(stepy))])
 
    while(path!=[]):
        current = path.pop(0)
        if(current.visited == False):
            current.visited = True
            print('c',current.x,current.y,current.x+current.y*(stepy))

            if(current.x+(current.y-1)*(stepy) > 0):
                top = agents[current.x+(current.y-1)*(stepy)]
                if(top.isWall == False and top.visited == False):
                    top.childof = 1
                    path.append(top)
                    print('t',top.x, top.y,top.x+top.y*stepy)

            if(current.x+current.y*(stepy)+1 < max_index):
                right = agents[(current.x+1)+current.y*(stepy)]
                if(right.isWall == False and right.visited == False):
                    right.childof = 2
                    path.append(right)
                    print('r',right.x, right.y,right.x+right.y*stepy)

            if(current.x+current.y*(stepy)-1 > 0):
                left = agents[(current.x-1)+current.y*(stepy)]
                if(left.isWall == False and left.visited == False):
                    left.childof = 0
                    path.append(left)
                    print('l',left.x, left.y, left.x+left.y*stepy)

            if(current.x+(current.y+1)*(stepy)< max_index):
                bottom = agents[current.x+(current.y+1)*(stepy)]
                if(bottom.isWall == False and bottom.visited == False):
                    bottom.childof = 3
                    path.append(bottom)
                    print('b',bottom.x, bottom.y,bottom.x+bottom.y*stepy)

            if(current.x == endPoint[0] and current.y  == endPoint[1]):
                    break

            itr =  itr+1
            grid = current.draw(zero)
#            cv2.imwrite(os.path.join(dir_path,'Floodfill/Image'+str(int(itr))+'.jpg'),grid)

    for agent in agents:
        if agent.visited == True:
             grid = agent.draw(inverted)

# cv2.imshow('Zero',zero)
    cv2.imshow('Grid',grid)
    print('itr =',itr)

    print('finding childs now')

    path = []
    path.append(current)
    prev_index = current.childof

    resultlength = 0
    while(path!=[]):
        current = path.pop(0)
        nextindex = current.childof
        #print(current.x,current.y,nextindex)

        if(prev_index != nextindex):
            if(prev_index == 0):
                print_direction = 'W'
            elif(prev_index == 1):
                print_direction = 'N'
            elif(prev_index == 2):
                print_direction = 'E'
            elif(prev_index == 3):
                print_direction = 'S'
            direction = prev_index
            prev_index = nextindex

            result.append(str(direction))
            show.append(print_direction)

        results = current.draw(results)
#        cv2.imwrite(os.path.join(dir_path,'Result/Image'+str(int(resultlength))+'.jpg'),results)

        if(current.x == startPoint[0] and current.y  == startPoint[1]):
                print('reached end')
                break

        if(nextindex == 0):
            nextNode = agents[(current.x+1)+current.y*(stepy)]
        elif(nextindex == 1):
            nextNode = agents[current.x+(current.y+1)*(stepy)]
        elif(nextindex == 2):
            nextNode = agents[(current.x-1)+current.y*(stepy)]
        elif(nextindex == 3):
            nextNode = agents[current.x+(current.y-1)*(stepy)]

        path.append(nextNode)
        resultlength = resultlength+1


    cv2.imshow('Result',results)
    result.reverse()
    show.reverse()

    to_send = ''.join(result)
    to_send = to_send+'6'

    print(to_send)

    print(show)
    s1.write(to_send.encode())

    if cv2.waitKey(0) & 0xff == 27:
        cv2.destroyAllWindows()