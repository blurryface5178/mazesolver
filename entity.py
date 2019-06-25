import cv2
import constants as CONST

class entity:
    x,y = 0,0
    childof = 1
    visited = False
    fill = 255
    isWall = True

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def draw(self,img):
        return cv2.rectangle(img,(self.x*CONST.w,self.y*CONST.w),(self.x*CONST.w+CONST.w,self.y*CONST.w+CONST.w),self.fill)
