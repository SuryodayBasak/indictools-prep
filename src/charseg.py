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
cv2.imshow('Output0',img1)
prep_img1 = prep2.binary_img(img1)
cv2.imshow('Output1',prep_img1)

dilate_sobel = cv2.dilate(prep_img1,kernel1,iterations = 1)
cv2.imshow('dilate sobel',dilate_sobel)

contours, hierarchy = cv2.findContours(dilate_sobel,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
for c in contours:
    x,y,w,h = cv2.boundingRect(c)
    cv2.rectangle(dilate_sobel,(x,y),(x+w,y+h),(0,0,0),2)

cv2.imshow('dilate sobel2',dilate_sobel)
cv2.waitKey(0)
cv2.destroyAllWindows()