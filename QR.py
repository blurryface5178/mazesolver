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
		text = barcode.data.decode("utf-8")
		cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 255), 2)
		cv2.imshow("Image", image)
		centerx = x,w
		centery = y,h
		print(str(text))
		cv2.putText(image, str(text), (x+w, y), cv2.FONT_HERSHEY_SIMPLEX, .5, (255,0,0), 2)

		QRs.append([str(text),centerx,centery])
		
	


	cv2.waitKey(0)
	return QRs
