import cv2
import numpy as np
from entity import entity

agents = []

filename = 'Maze.png'
img = cv2.imread(filename)
img = cv2.resize(img, (256,256))

rows, cols, ch = img.shape
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
zero = np.zeros((rows,cols),dtype=np.uint8)
cv2.imshow('dst',img)

agents[0] = entity(125,255)
for agent in agents:
    if(agent.x)


zero = one.draw(zero)
cv2.imshow('zero',zero)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
