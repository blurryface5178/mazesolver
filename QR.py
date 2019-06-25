import cv2
from pyzbar import pyzbar

#image = cv2.imread('MazeQR.jpg')
#image = image.resize(1024,1024)

QRs= []
points = []

def decodeQR(image):
	barcodes = pyzbar.decode(image)
	
	text = ""
	
	for barcode in barcodes:
		#for point in barcode.polygon:	
		#        points.append(point)
		(x, y, w, h) = barcode.rect
		cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 255), 2)
		cv2.imshow("Image", image)
		centerx = x+w/2
		centery = y+h/2

		QRs.append([centerx,centery])
		
	
	#cv2.putText(image, str(text), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, .5, (255, 255, 255), 2)

	cv2.waitKey(0)
	return QRs
