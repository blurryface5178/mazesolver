import cv2

w = 1

class entity:
    x = 0
    y = 0
    childof = 0

    def __init__(self,x,y,childof):
        self.x = x
        self.y = y
        self.childof = childof

    def draw(self,img):
        return cv2.rectangle(img,(self.x-int(w/2),self.y-int(w/2)),(self.x+int(w/2),self.y+int(w/2)),127,1)
