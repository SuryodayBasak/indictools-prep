# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 20:57:44 2015

@author: suryo
"""

import cv2
import numpy as np
import prep3
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))

img = cv2.imread('/home/suryo/Image_Processing_Exercises/indictools-prep/resources/clips/1.jpg',0)
height, width = img.shape
base = np.ones(img.shape[:2],np.uint8)
print height,width

#th3 = prep3.binary_img(img)

cl1 = clahe.apply(img)
cv2.imshow('cl1',cl1)
blur = cv2.GaussianBlur(cl1,(3,3),0)
ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow('bina',th3)


x= 10
y = 22
w = 60
h = 60
image = img[y:y + h, x:x + w]
cv2.imshow('img',image)


for i in range(0,height,h):
    for j in range(0,width,w):
        print (j,i)
        #cv2.rectangle(img,(j,i),(j+w,i+h),(0,0,255),2)
        image = img[i:i+w,j:j+h]
        
        cl1 = clahe.apply(image)
        blur = cv2.GaussianBlur(cl1,(3,3),0)
        ret,th = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        base[i:i+w,j:j+h] = th
        
        #print img
#cv2.imshow('img1',th)        
cv2.imshow('img',img)
cv2.imshow('base',base)

cv2.waitKey(0)
cv2.destroyAllWindows()