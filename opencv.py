import cv2
import numpy as np
from entity import entity
import time

agents = []
radius = 1
dia = radius*2

def creatNewAgent(x,y,childof):
    if not(x==int(rows/2) and y==0):
        newAgent = entity(x,y,childof)
        agents.append(newAgent)
    else:
        print("haha")

def clearStack(index):
    for i in range(index,len(agents)-1):
        agents[i] = agents[i+1]

if __name__ == '__main__':
    filename = 'Maze.png'
    img = cv2.imread(filename)
    img = cv2.resize(img, (256,256))

    rows, cols, _ = img.shape
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    _, gray = cv2.threshold(gray, 250, 255, cv2.THRESH_BINARY)
    zero = np.zeros((rows,cols),dtype=np.uint8)
    cv2.imshow('dst',img)

    creatNewAgent(int(rows/2),int(cols)-1,1)

    for index,agent in enumerate(agents):
        if(agent.x>0 and agent.x<rows and agent.y>0 and agent.y<cols):
            if(gray[agent.x,agent.y]==255):
                print(agent.x,agent.y,agent.childof)
                if(agent.childof == 0):
                    creatNewAgent(agent.x-dia,agent.y,0)
                elif(agent.childof == 2):
                    creatNewAgent(agent.x+dia,agent.y,2)
                elif(agent.childof == 1):
                    creatNewAgent(agent.x-dia,agent.y,0)
                    creatNewAgent(agent.x,agent.y-dia,1)
                    creatNewAgent(agent.x+dia,agent.y,2)
            else:
                clearStack(index)


            zero = agent.draw(zero)
            cv2.imshow('zero',zero)

            #clearStack()

    if cv2.waitKey(0) & 0xff == 27:
        cv2.destroyAllWindows()
