# -*- coding: utf-8 -*-
"""
Created on Tue May 26 22:07:47 2015

@author: suryo
"""

import cv2
import prep2
import numpy as np
from scipy.stats import mode

img1 = cv2.imread('/home/suryo/Image_Processing_Exercises/IISC/resources/Kandanu10.jpg',0)
words = np.zeros(img1.shape[:2],np.uint8)

cv2.imshow('Output0',img1)
prep_img1 = prep2.binary_img(img1)
cv2.imshow('Output1',prep_img1)
cv2.imwrite('skewres1_prec.jpg',prep_img1)

sobely = cv2.Sobel(prep_img1,cv2.CV_64F,0,1,ksize=5)
abs_sobel64f = np.absolute(sobely)
sobel_8u = np.uint8(abs_sobel64f)

cv2.imshow('Output2',sobel_8u)

minLineLength = 100
maxLineGap = 10
lines = cv2.HoughLinesP(sobel_8u,1,np.pi/180,100,minLineLength,maxLineGap)

for x1,y1,x2,y2 in lines[0]:
    cv2.line(words,(x1,y1),(x2,y2),(255,255,255),2)
cv2.imshow('hough',words)

















height_orig, width_orig = img1.shape[:2]
all_angles = []



contours, hierarchy = cv2.findContours(words,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print len(contours)
contour_count=0;   
for c in contours:
    #max_index = np.argmax(areas)
    #current_contour = np.zeros(img.shape[:2],np.uint8)
    current_contour = np.zeros(img1.shape[:2],np.uint8)
    cv2.drawContours(current_contour, contours, contour_count, (255,255,255), -1)

    height, width = current_contour.shape[:2]

    all_white_pixels = []
    current_white_pixels = [] 

    for i in range(0,height):
        for j in range(0,width):
            if(current_contour.item(i,j)==255):
                current_white_pixels.append([i,j])
            

    matrix = np.array(current_white_pixels)
    
    """Finding covariance matrix"""
    C = np.cov(matrix.T)

    eigenvalues, eigenvectors = np.linalg.eig(C)

    """Finding max eigenvalue"""
    max_ev = max(eigenvalues)
    """Finding index of max eigenvalue"""
    max_index =  eigenvalues.argmax(axis=0)

    """The largest eigen value gives the approximate length of the bounding
    ellipse around the largest word. If we follow the index of the largest 
    eigen value and find the eigen vectors in the column of that index,
    we'll get the x and y coordinates of it's centre."""
    y = eigenvectors[1,max_index]
    x = eigenvectors[0,max_index]

    angle = (np.arctan2(y,x))*(180/np.pi)
    all_angles.append(angle)
    contour_count+=1
    print contour_count
    
print all_angles
angle = np.mean(all_angles)
print angle
    
k = 0;
non_zero_angles = []
    
for i in all_angles:
    if ((i != 0) and (i!=90.0)):
        non_zero_angles.append(i)
            
print non_zero_angles
    
rounded_angles = []
for i in non_zero_angles:
    rounded_angles.append(np.round(i,0))
    
print rounded_angles
print "mode is"
#print np.mode(rounded_angles)
#angle = np.mean(non_zero_angles)
#angle = np.mode(rounded_angles)
    
mode_angle = mode(rounded_angles)[0][0]
print mode_angle
    
precision_angles = []
for i in non_zero_angles:
    if (np.round(i,0) == mode_angle):
        precision_angles.append(i)
            
print 'precision angles:'
print precision_angles
    
angle = np.mean(precision_angles)
print 'Finally, the required angle is:'
print angle
    
#M = cv2.getRotationMatrix2D((width/2,height/2),-(90+angle),1)
M = cv2.getRotationMatrix2D((width/2,height/2),-(90+angle),1)
dst = cv2.warpAffine(img1,M,(width_orig,height_orig))
    
cv2.imshow('final',dst)
cv2.imwrite('skewcorrected.jpg',dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

