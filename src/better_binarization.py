# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 20:57:44 2015

@author: suryo
"""

import cv2
import numpy as np
import prep3
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))

img = cv2.imread('/home/suryo/Image_Processing_Exercises/indictools-prep/resources/clips/crop1_1.jpg',0)
#th3 = prep3.binary_img(img)

cl1 = clahe.apply(img)
cv2.imshow('cl1',cl1)
blur = cv2.GaussianBlur(cl1,(3,3),0)
ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imshow('bina',th3)

cv2.waitKey(0)
cv2.destroyAllWindows()