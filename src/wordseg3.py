# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 16:53:42 2015

@author: suryo
"""


import cv2
import prep2
import numpy as np
kernel1 = np.ones((2,3),np.uint8)
kernel2 = np.ones((1,1),np.uint8)

all_heights = [] 
img = cv2.imread('/home/suryo/Image_Processing_Exercises/indictools-prep/resources/2.jpg',0)
cv2.imshow('Output0',img)
words_temp = np.zeros(img.shape[:2],np.uint8)

binary = prep2.binary_img(img)

sobelx = cv2.Sobel(binary,cv2.CV_64F,1,0,ksize=5)
cv2.imshow('sobel',sobelx)
dilate_sobel = cv2.dilate(binary,kernel1,iterations = 1)
cv2.imshow('dilate sobel',dilate_sobel)

dilation = cv2.dilate(binary,kernel1,iterations = 1)
erosion = cv2.dilate(dilation,kernel1,iterations = 1)

cv2.imshow('d',erosion)

"""
contours, hierarchy = cv2.findContours(erosion,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for xx in contours:
    cv2.drawContours(words_temp,[xx],-1,(255,255,255),-1)
cv2.imshow('Outputtemp0',words_temp)
    
contours, hierarchy = cv2.findContours(words_temp,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
for c in contours:
    x,y,w,h = cv2.boundingRect(c)
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,0),2)

cv2.imshow('Outputimg2',img)
"""

contours, hierarchy = cv2.findContours(dilate_sobel,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for xx in contours:
    cv2.drawContours(words_temp,[xx],-1,(255,255,255),-1)
cv2.imshow('Outputtemp0',words_temp)
    
contours, hierarchy = cv2.findContours(words_temp,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
for c in contours:
    x,y,w,h = cv2.boundingRect(c)
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,0),2)

cv2.imshow('Outputimg2',img)
          
cv2.waitKey(0)
cv2.destroyAllWindows()