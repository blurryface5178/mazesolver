import cv2
import numpy as np
import entity

entity = entity.entity

w = 1
agents = []
reachedend = 0

filename = 'Maze.png'
img = cv2.imread(filename)
img = cv2.resize(img, (256,256))
rows, cols, _ = img.shape
gray = np.zeros((rows,cols),dtype=np.uint8)

def collision(x,y):
    min_x = x-w
    max_x = x+w
    min_y = y-w
    max_y = y+w

    print(x,y)
    if (gray[min_x,min_y]==0 or gray[max_x,min_y]==0):
        if(gray[min_x,max_y]==0 or gray[max_x,max_y]==0):
            return True

def creatNewAgent(x,y,childof):
#    if not collision(x,y):
        newAgent = entity(x,y,childof)
        agents.append(newAgent)


def clearStack(index):
    for i in range(index,len(agents)-1):
        agents[i] = agents[i+1]

if __name__ == '__main__':
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    _, gray = cv2.threshold(gray, 250, 255, cv2.THRESH_BINARY)
    zero = np.zeros((rows,cols),dtype=np.uint8)
    cv2.imshow('dst',img)

    creatNewAgent(int(rows/2),int(cols)-2,1)

    for index,agent in enumerate(agents):
        if (reachedend == 0):
            if(agent.x>0 and agent.x<rows and agent.y>0 and agent.y<cols):
                if not collision(agent.x, agent.y):
                    creatNewAgent(agent.x,agent.y-w,1)
                    if(agent.childof == 0):
                        creatNewAgent(agent.x-w,agent.y,0)
                    elif(agent.childof == 2):
                        creatNewAgent(agent.x+w,agent.y,2)
                    elif(agent.childof == 1):
                        creatNewAgent(agent.x-w,agent.y,0)
                        creatNewAgent(agent.x+w,agent.y,2)

                    zero = agent.draw(zero)
                else:
                    clearStack(index)

        if (agent.x==int(rows/2) and agent.y==0):
            reachedend = 1
            print('haha')

    cv2.imshow('zero',zero)
                #clearStack()

    if cv2.waitKey(0) & 0xff == 27:
        cv2.destroyAllWindows()
