from cv2 import imread
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import matplotlib.image as maing

from PIL import Image
from PIL import ImageEnhance




class Imgpor:
    
    def __init__(self,img) -> None:
        #self.img=img
        self.img=cv.imread(img)


    def enhance(self):
        im=Image.open("f4.jpg")
        ImageEnhance.Contrast(im)
        curr_con = ImageEnhance.Contrast(im)
        new_con = 17.0
        img_contrasted = curr_con.enhance(new_con) 

        curr_sharp = ImageEnhance.Sharpness(img_contrasted)
        new_sharp = 10.0
  

        img_sharped = curr_sharp.enhance(new_sharp)
  

        curr_bri = ImageEnhance.Brightness(img_sharped)
        new_bri = 8.5

  

        img_brightened = curr_bri.enhance(new_bri)
  


        curr_col = ImageEnhance.Color(img_brightened)
        new_col = 3.5

        img_colored = curr_col.enhance(new_col)
  

        img_colored.show()
        self.img=img_colored
        
    def threshold(self):
        self.img = np.array(self.img)

        
        gray_img=cv.cvtColor(self.img,cv.COLOR_BGR2GRAY)
        adap = cv.adaptiveThreshold(gray_img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY_INV, 31, 5)
        cv.imshow('Threshold',adap)
        cv.waitKey(0)
    


#img=cv.imread('Kodikon/ImagesK/kindanice.jpeg')
i1=Imgpor('f4.jpg')

i1.enhance()
i1.threshold()