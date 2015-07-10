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
img = cv2.imread('/home/suryo/Image_Processing_Exercises/indictools-prep/resources/2.jpg',0)
cv2.imshow('Output0',img)
words_temp = np.zeros(img.shape[:2],np.uint8)

binary = prep2.binary_img(img)
cv2.imshow('Outputimg1',binary)

dilation = cv2.dilate(binary,kernel1,iterations = 1)
cv2.imshow('Outputimg2',dilation)
          
cv2.waitKey(0)
cv2.destroyAllWindows()