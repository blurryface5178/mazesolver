import cv2
radius = 1

class entity:
    x = 0
    y = 0
    childof = 0

    def __init__(self,x,y,childof):
        self.x = x
        self.y = y
        self.childof = childof

    def draw(self,img):
        return cv2.circle(img,(self.x,self.y),radius,127,-1)
