# -*- coding: utf-8 -*-
"""
Created on Tue May  3 21:38:31 2016

@author: Administrator
"""

import numpy 
import cv2
from matplotlib import pyplot as plt


# Load an color image in grayscale
img = cv2.imread("D:\\360Downloads\\4574221604353026.jpeg",0)

cv2.imshow('image',img)
#k = cv2.waitKey(0)
#if k == 27:         # wait for ESC key to exit
#    cv2.destroyAllWindows()
#elif k == ord('s'): # wait for 's' key to save and exit
#    cv2.imwrite('messigray.png',img)
#    cv2.destroyAllWindows()
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()
