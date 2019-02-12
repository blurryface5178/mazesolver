import cv2

class entity:
    x = 0
    y = 0
    status = 0

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.status = 0

    def draw(self,img):
        return cv2.circle(img,(self.x,self.y),1,255)
