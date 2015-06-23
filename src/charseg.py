# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 17:10:45 2015

@author: suryo
"""

import cv2
import prep2
import numpy as np
kernel1 = np.ones((3,3),np.uint8)


img1 = cv2.imread('/home/suryo/Image_Processing_Exercises/indictools-prep/resources/Kandanuword.jpg',0)
words_temp = np.zeros(img1.shape[:2],np.uint8)

cv2.imshow('Original Image',img1)

prep_img1 = prep2.binary_img(img1)
cv2.imshow('Binarized Image',prep_img1)

dilate1 = cv2.dilate(prep_img1,kernel1,iterations = 1)
cv2.imshow('Dilated',dilate1)

contours, hierarchy = cv2.findContours(dilate1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
for xx in contours:
    cv2.drawContours(words_temp,[xx],-1,(255,255,255),-1)
cv2.imshow('Contours from Dilated',words_temp)

contours, hierarchy = cv2.findContours(words_temp,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
for c in contours:
    x,y,w,h = cv2.boundingRect(c)
    #cv2.rectangle(prep_img1,(x,y),(x+w,y+h),(255,0,0),1)
    
print x,y,w,h

for i in range(x,x+w):
    for j in range(y,y+w):
        try:
            if prep_img1[i,j] == 255:
                print (i,j)
                break
        except:
            pass
        
    for j in range(y+w,y,-1):
        try:
             if prep_img1[i,j] == 255:
                 print (i,j)
                 break
        except:
            pass
            
    print ""
    print ""
    print ""

cv2.imshow('Bounding Box',prep_img1)
cv2.waitKey(0)
cv2.destroyAllWindows()