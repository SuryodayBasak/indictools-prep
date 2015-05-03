# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 15:24:29 2015

@author: suryo
"""

import cv2
import prep2

"""
img1 = cv2.imread('/home/suryo/Image_Processing_Exercises/IISC/resources/1.jpg',0)
cv2.imshow('Output0',img1)
prep_img1 = prep2.preprocess(img1)
cv2.imshow('Output1',prep_img1)
cv2.imwrite('skewres1_prec.jpg',prep_img1)

img2 = cv2.imread('/home/suryo/Image_Processing_Exercises/IISC/resources/Kandanu10.jpg',0)
prep_img2 = prep2.preprocess(img2)
cv2.imshow('Outpu2t',prep_img2)
cv2.imwrite('skewres2_prec.jpg',prep_img2)
"""

img1 = cv2.imread('/home/suryo/Image_Processing_Exercises/indictools-prep/resources/IMG_3940.JPG',0)
cv2.imshow('Output0',img1)
prep_img1 = prep2.preprocess(img1)
cv2.imshow('Output1',prep_img1)
cv2.imwrite('skewres1_prec.jpg',prep_img1)

cv2.waitKey(0)
cv2.destroyAllWindows()

