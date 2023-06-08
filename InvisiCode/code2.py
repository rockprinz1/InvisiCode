import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar

img = cv2.imread('qr1.jpeg')
decodedObjects = pyzbar.decode(img)
for obj in decodedObjects:
    print('Type : ', obj.type)
    print('Data : ', obj.data,'\n')

cv2.imshow('Frame',img)

cv2.waitKey(0)