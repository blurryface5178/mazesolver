import cv2

w = 6

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
        return cv2.rectangle(img,(self.x*w,self.y*w),(self.x*w+w,self.y*w+w),self.fill)
