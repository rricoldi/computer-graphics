import cv2 as cv 
import sys
import numpy as np
import utils

image = cv.imread(sys.argv[1]) 

b, g, r = cv.split(image)

[c, m, y, k] = utils.get_cmyk_by_rgb(r, g, b)
utils.print_matrix_into_file('result.txt', cv.merge([c, m, y, k]))

cv.imshow("CMYK", cv.merge([c, m, y, k]))

cv.waitKey(0) 