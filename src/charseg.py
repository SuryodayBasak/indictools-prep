# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 17:10:45 2015

@author: suryo
"""

import cv2
import prep2
import numpy as np
import matplotlib.pyplot as plt
kernel1 = np.ones((3,3),np.uint8)


img1 = cv2.imread('/home/suryo/Image_Processing_Exercises/indictools-prep/resources/Kandanuword.jpg',0)
words_temp = np.zeros(img1.shape[:2],np.uint8)
print img1.shape[:2]
difference_values =[]
clipped_values= []
clipped_local_minima = []

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
"""
cv2.circle(prep_img1,(x,y), 5, (255,255,255), -1)
cv2.circle(prep_img1,(x+w,y+h), 5, (255,255,255), -1)
"""
print words_temp
print type(words_temp)
print words_temp[25,30]

cv2.imshow('Bounding Box0',words_temp)
for i in range(x,x+w):
    #print "Entered loop1"
    for j in range(y,y+h):
        #print "Entered loop2.1"
        if prep_img1[j,i] == 255:
            #if (words_temp[j,i] == 255):
            upper = j
            #print "Upper",upper
            break
        
    for j in range(y+h,y,-1):
        #print "Entered loop2.2"
        if prep_img1[j,i] == 255:
            #if (words_temp[j,i] == 255):
            lower = j
            #print "Lower",lower
            break
    try:    
        #print(i,lower-upper)
        difference_values.append((i,lower-upper))
    except:
        difference_values.append((i,0))
""" 
for (i,j) in difference_values:
    if j == 0:
        cv2.line(img1,(i,j+y),(i,j+y+h),(0,255,0),2)
"""     
print difference_values

avg1 = 0
count = 0
for (i,j) in difference_values:
    avg1+=j
    count+=1

print avg1 
avg1/=count

clipped_values_x = []
clipped_values_y = []
for (i,j) in difference_values:
    if j < avg1:
        clipped_values.append((i,j))
        clipped_values_x.append(i)
        clipped_values_y.append(j)
        
print clipped_values
print clipped_values_x
print clipped_values_y

count = 0

for idx, val in enumerate(clipped_values_y):
    #print idx, val
    try:
        if (clipped_values_y[idx]<clipped_values_y[idx-1]) and (clipped_values_y[idx]<clipped_values_y[idx+1]):
            clipped_local_minima.append((clipped_values_x[idx],clipped_values_y[idx]))
    except:
        pass

print ''
print ''
print clipped_local_minima


for (i,j) in clipped_local_minima:
    cv2.line(img1,(i,j+y),(i,j+y+h),(0,255,0),2)
   
plt.plot(*zip(*clipped_values))
plt.show()
cv2.imshow('Bounding Box',img1)
cv2.imwrite('charsegmentation1.jpg',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()