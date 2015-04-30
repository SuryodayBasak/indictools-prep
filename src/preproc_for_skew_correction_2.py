# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 19:08:52 2015

@author: suryo
"""

import cv2
import binarization
import numpy as np
kernel = np.ones((5,5),np.uint8)

img = cv2.imread('/home/suryo/Image_Processing_Exercises/IISC/resources/1.jpg',0)
cv2.imshow('original', img)
largest_contour = np.zeros(img.shape[:2],np.uint8)

binary = binarization.binary_img(img)
cv2.imshow('binary', binary)

#contours, hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
contours, hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
areas = [cv2.contourArea(c) for c in contours]
max_index = np.argmax(areas)
cnt=contours[max_index]

print max_index

cv2.drawContours(largest_contour, contours, max_index, (255,255,255), 2)
cv2.imshow('largest', largest_contour)
#cv2.imwrite('largest.jpg', mask)



height, width = largest_contour.shape[:2]

all_white_pixels = []

print height
print width

for i in range(0,height):
    for j in range(0,width):
        if(largest_contour.item(i,j)==255):
            all_white_pixels.append([i,j])
            
#print all_white_pixels
matrix = np.array(all_white_pixels)

#row_mean = matrix.mean(axis=1) 
#col_mean = matrix.mean(axis=0) 

#print row_mean
#print col_mean

C = np.cov(matrix.T)
print C

eigenvalues, eigenvectors = np.linalg.eig(C)

print eigenvalues
print eigenvectors

max_ev = max(eigenvalues)
max_index =  eigenvalues.argmax(axis=0)
#print type(eigenvalues)
print max_ev
print max_index

print (eigenvectors[1,max_index]/eigenvectors[0,max_index])*(180/np.pi)
#print math.atan2((eigenvectors[1,max_index],eigenvectors[0,max_index]))*(180/np.pi)

y = eigenvectors[1,max_index]
x = eigenvectors[0,max_index]

"""
y = eigenvectors[max_index,1]
x = eigenvectors[max_index,0]
"""
angle = (np.arctan2(y,x))*(180/np.pi)

print angle

#M = cv2.getRotationMatrix2D((width/2,height/2),-angle/2,1)
M = cv2.getRotationMatrix2D((width/2,height/2),-(90+angle),1)
dst = cv2.warpAffine(img,M,(width,height))

print type(dst)

cv2.imshow('dst', dst)
dst = binarization.binary_img(dst)
cv2.imwrite('skewcorrected.jpg',dst)



cv2.waitKey(0)
cv2.destroyAllWindows()