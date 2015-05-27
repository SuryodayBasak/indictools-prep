# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 15:24:29 2015

@author: suryo
"""

import cv2
import prep2

img1 = cv2.imread('/home/suryo/Image_Processing_Exercises/IISC/resources/Kandanu10.jpg',0)
cv2.imshow('Output0',img1)
prep_img1 = prep2.preprocess(img1)
cv2.imshow('Output1',prep_img1)
cv2.imwrite('skewres1_prec.jpg',prep_img1)

cv2.waitKey(0)
cv2.destroyAllWindows()

