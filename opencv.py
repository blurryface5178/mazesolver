import cv2
import numpy as np
import entity
import time

entity = entity.entity

w = 6
agents = []
path = []
result = []
kernel = np.ones((3,3), np.uint8)

filename = 'Maze.png'
img = cv2.imread(filename)
img = cv2.resize(img, (216,216))

rows, cols, _ = img.shape
steps = int(rows/w)

startPoint = [int((cols/2)/w),int((rows/w)-1)]
endPoint = [int((cols/2)/w),0]

grid = np.zeros((rows,cols),dtype=np.uint8)
zero = np.zeros((rows,cols),dtype=np.uint8)
result = np.zeros((rows,cols),dtype=np.uint8)

def collision(x,y):
    minX, minY = x*w,y*w
    for j in range(minY,minY+w):
        for i in range(minX,minX+w):
            if (gray[j,i]==0):
                return True
            else:
                return False

def creatNewAgent(x,y):
    newAgent = entity(x,y)
    if not collision(x,y):
        newAgent.fill = 127
        newAgent.isWall = False
    agents.append(newAgent)

if __name__ == '__main__':
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    _, gray = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    gray = cv2.erode(gray,kernel,iterations=2)
    #gray = cv2.dilate(gray,kernel, iterations=4)
    inverted = cv2.bitwise_not(gray)
    for j in range(steps):
        for i in range(steps):
            creatNewAgent(i,j)

    max_index = len(agents)
    itr = 0

    path.append(agents[startPoint[0]+startPoint[1]*(steps)])
    while(path!=[]):
        current = path.pop(0)
        if(current.visited == False):
            current.visited = True
            print('c',current.x,current.y,current.x+current.y*(steps))

            if(current.x+(current.y-1)*(steps) > 0):
                top = agents[current.x+(current.y-1)*(steps)]
                if(top.isWall == False and top.visited == False):
                    top.childof = 1
                    path.append(top)
                    print('t',top.x, top.y,top.x+top.y*steps)

            if(current.x+current.y*(steps)+1 < max_index):
                right = agents[(current.x+1)+current.y*(steps)]
                if(right.isWall == False and right.visited == False):
                    right.childof = 2
                    path.append(right)
                    print('r',right.x, right.y,right.x+right.y*steps)

            if(current.x+current.y*(steps)-1 > 0):
                left = agents[(current.x-1)+current.y*(steps)]
                if(left.isWall == False and left.visited == False):
                    left.childof = 0
                    path.append(left)
                    print('l',left.x, left.y, left.x+left.y*steps)

            if(current.x+(current.y+1)*(steps)< rows):
                bottom = agents[current.x+(current.y+1)*(steps)]
                if(bottom.isWall == False and bottom.visited == False):
                    bottom.childof = 3
                    path.append(bottom)
                    print('b',bottom.x, bottom.y,bottom.x+bottom.y*steps)

            if(current.x == endPoint[0] and current.y  == endPoint[1]):
                    break

            itr =  itr+1
            grid = current.draw(zero)
            cv2.imwrite('Image'+str(int(itr))+'.jpg',grid)

    for agent in agents:
        if agent.visited == True:
             grid = agent.draw(inverted)

# cv2.imshow('Zero',zero)
    cv2.imshow('Grid',grid)
    print('itr =',itr)

    print('finding childs now')

    path = []
    path.append(current)

    resultlength = 0
    while(path!=[]):
        current = path.pop(0)
        nextindex = current.childof
        print(current.x,current.y,nextindex)

        result = current.draw(result)
        cv2.imwrite('Result'+str(int(resultlength))+'.jpg',result)

        if(current.x == startPoint[0] and current.y  == startPoint[1]):
                print('reached end')
                break

        if(nextindex == 0):
            nextNode = agents[(current.x+1)+current.y*(steps)]
        elif(nextindex == 1):
            nextNode = agents[current.x+(current.y+1)*(steps)]
        elif(nextindex == 2):
            nextNode = agents[(current.x-1)+current.y*(steps)]
        elif(nextindex == 3):
            nextNode = agents[current.x+(current.y-1)*(steps)]

        path.append(nextNode)
        resultlength = resultlength+1
        #result.append(nextNode)


    cv2.imshow('Result',result)
    print(resultlength)
        #checkNeighborEmpty()
        #expandToEmptyNeighbor()

    if cv2.waitKey(0) & 0xff == 27:
        cv2.destroyAllWindows()
