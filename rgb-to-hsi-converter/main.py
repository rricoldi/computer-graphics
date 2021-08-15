import cv2 as cv 
import sys
import numpy as np
import utils

# image = cv.imread(sys.argv[1]) 

# r, g, b = cv.split(image)

[h, s, i] = utils.get_hsi_by_rgb(66, 135, 245)

print(h, s, i)

# cv.imshow("CMYK", cv.merge([c, m, y, k]))

# cv.waitKey(0) 

# HSI = (218, 0.556, 0.583);