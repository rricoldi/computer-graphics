import cv2 as cv 
import sys
import numpy as np
import utils

image = cv.imread(sys.argv[1]) 

b, g, r = cv.split(image)

hsi_image = utils.get_hsi_by_rgb(r, g, b)

utils.print_matrix_into_file('result.txt', hsi_image)

cv.imshow("HSI", hsi_image)

cv.waitKey(0) 