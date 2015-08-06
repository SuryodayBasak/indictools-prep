# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 23:05:13 2015

@author: suryo
"""

import prep3
import cv2

img1 = cv2.imread('/home/suryo/Image_Processing_Exercises/indictools-prep/resources/book2/o5.jpg',0)
prep3.skew_correction(img1)