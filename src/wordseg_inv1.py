# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 15:22:33 2015

@author: suryo
"""

import cv2
import prep2
import numpy as np
kernel1 = np.ones((2,2),np.uint8)
kernel2 = np.ones((1,1),np.uint8)

all_heights = [] 
img = cv2.imread('/home/suryo/Image_Processing_Exercises/indictools-prep/resources/pl8.jpg',0)
cv2.imshow('Output0',img)
words_temp = np.zeros(img.shape[:2],np.uint8)

binary = prep2.binary_img(img)
cv2.imshow('Outputimg1',binary)

dilation = cv2.dilate(binary,kernel1,iterations = 1)
cv2.imshow('Outputimg2',dilation)

erosion = cv2.dilate(dilation,kernel1,iterations = 1)
cv2.imshow('Outputimg3',erosion)

edges = cv2.Canny(dilation,50,100)
cv2.imshow('edges',edges)          

edges = cv2.dilate(edges,kernel1,iterations = 1)
ret,thresh = cv2.threshold(edges,127,255,0)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for xx in contours:
    cv2.drawContours(edges,[xx],-1,(255,255,255),-1)
    
cv2.imshow('edges2',edges)


cv2.waitKey(0)
cv2.destroyAllWindows()