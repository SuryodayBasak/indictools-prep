# -*- coding: utf-8 -*-
"""
Created on Wed May 27 22:52:39 2015

@author: suryo
"""

import cv2
import prep2
import numpy as np
import math
kernel1 = np.ones((2,3),np.uint8)
kernel2 = np.ones((1,1),np.uint8)

all_heights = [] 
img = cv2.imread('/home/suryo/Image_Processing_Exercises/indictools-prep/resources/Kandanu1.jpg',0)
cv2.imshow('Output0',img)
words_temp = np.zeros(img.shape[:2],np.uint8)

binary = prep2.binary_img(img)

dilation = cv2.dilate(binary,kernel1,iterations = 1)
erosion = cv2.dilate(dilation,kernel1,iterations = 1)

cv2.imshow('d',erosion)

contours, hierarchy = cv2.findContours(erosion,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for xx in contours:
    cv2.drawContours(words_temp,[xx],-1,(255,255,255),-1)
cv2.imshow('Outputtemp0',words_temp)
    
contours, hierarchy = cv2.findContours(words_temp,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
for c in contours:
    x,y,w,h = cv2.boundingRect(c)
    #img = 
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,0),2)
    cv2.imshow('Outputimg2',img)
    #all_heights.append(h)
    
"""
contours, hierarchy = cv2.findContours(words_temp,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
for c in contours:
    x,y,w,h = cv2.boundingRect(c)
    #img = 
    #cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,0),2)
    all_heights.append(h)

print all_heights
mean_height = np.mean(all_heights)
print mean_height
std_dev = np.std(all_heights)
print std_dev

for c in contours:
    x,y,w,h = cv2.boundingRect(c)
    if(math.fabs(h-mean_height)<=(std_dev)):
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,0),2)
        cv2.rectangle(words_temp,(x,y),(x+w,y+h),(0,0,0),-1)

cv2.imshow('Outputimg',img)
cv2.imshow('Outputtemp',words_temp)
#cv2.imwrite('wordseg3.jpg',img)

contours, hierarchy = cv2.findContours(words_temp,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for xx in contours:
    cv2.drawContours(words_temp,[xx],-1,(255,255,255),-1)
cv2.imshow('Outputtempk',words_temp)
words_temp2=words_temp

all_heights2 = []
contours, hierarchy = cv2.findContours(words_temp2,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
for c in contours:
    x,y,w,h = cv2.boundingRect(c)
    #img = 
    #cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,0),2)
    all_heights2.append(h)

print all_heights
mean_height = np.mean(all_heights2)
print mean_height
std_dev = np.std(all_heights2)
print std_dev

for c in contours:
    x,y,w,h = cv2.boundingRect(c)
    if(math.fabs(h-mean_height)<=(std_dev)):
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,0),2)
        cv2.rectangle(words_temp,(x,y),(x+w,y+h),(0,0,0),-1)

cv2.imshow('Outputimg2',img)
cv2.imshow('Outputtemp2',words_temp)
"""        
            
cv2.waitKey(0)
cv2.destroyAllWindows()