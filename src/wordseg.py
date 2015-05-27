# -*- coding: utf-8 -*-
"""
Created on Wed May 27 22:52:39 2015

@author: suryo
"""

import cv2
import prep2
import numpy as np
kernel = np.ones((2,4),np.uint8)


img = cv2.imread('/home/suryo/Image_Processing_Exercises/indictools-prep/resources/durga.jpg',0)
cv2.imshow('Output0',img)
words_temp = np.zeros(img.shape[:2],np.uint8)

binary = prep2.binary_img(img)

dilation = cv2.dilate(binary,kernel,iterations = 1)
cv2.imshow('d',dilation)

contours, hierarchy = cv2.findContours(dilation,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for xx in contours:
    cv2.drawContours(words_temp,[xx],-1,(255,255,255),-1)
cv2.imshow('Outputtemp0',words_temp)
    
contours, hierarchy = cv2.findContours(words_temp,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
for c in contours:
    x,y,w,h = cv2.boundingRect(c)
    #img = 
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,0),2)

cv2.imshow('Outputtemp',img)
cv2.imwrite('wordseg3.jpg',img)

            
            
cv2.waitKey(0)
cv2.destroyAllWindows()