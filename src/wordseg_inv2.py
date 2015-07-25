# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 20:34:24 2015

@author: suryo
"""

import cv2
import prep2
import numpy as np
kernel1 = np.ones((2,2),np.uint8)
kernel2 = np.ones((1,1),np.uint8)

all_heights = [] 
img = cv2.imread('/home/suryo/Image_Processing_Exercises/indictools-prep/resources/book2/o8.jpg',0)
cv2.imshow('Output0',img)
words_temp = np.zeros(img.shape[:2],np.uint8)
boxes_temp = np.zeros(img.shape[:2],np.uint8)

binary = prep2.binary_img(img)
cv2.imshow('Outputimg1',binary)

dilation = cv2.dilate(binary,kernel1,iterations = 1)
cv2.imshow('Outputimg2',dilation)

erosion = cv2.dilate(dilation,kernel1,iterations = 1)
cv2.imshow('Outputimg3',erosion)

edges = cv2.Canny(dilation,50,100)
cv2.imshow('edges',edges)          

dilation2 = cv2.dilate(edges,kernel1,iterations = 1)
cv2.imshow('Outputimg9999',dilation2)

inv9999 = 255-dilation2
cv2.imshow('inv9999',inv9999)

edges = cv2.dilate(edges,kernel1,iterations = 1)
ret,thresh = cv2.threshold(erosion,127,255,0)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for c in contours:
    x,y,w,h = cv2.boundingRect(c)
    #cv2.rectangle(boxes_temp,(x,y),(x+w,y+h),(255,255,255),-1)
    if h> 10:
        all_heights.append(h)

print all_heights
std_dev = np.std(all_heights)
mn = np.mean(all_heights)
md = np.median(all_heights)
print std_dev,mn, md

for xx in contours:
    cv2.drawContours(edges,[xx],-1,(255,255,255),-1)
    
cv2.imshow('edges2',edges)








ret,thresh = cv2.threshold(erosion,127,255,0)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for c in contours:
    x,y,w,h = cv2.boundingRect(c)
    #if (mn+(std_dev/2)<h):
    cv2.rectangle(boxes_temp,(x,y),(x+w,y+h),(255,0,0),-1)
    #cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    
cv2.imshow('boxes_temp',boxes_temp)


ret,thresh = cv2.threshold(boxes_temp,127,255,0)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for c in contours:
    x,y,w,h = cv2.boundingRect(c)
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()