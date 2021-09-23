import cv2 as cv 
import sys
import numpy as np
import utils

image = cv.imread(sys.argv[1]) 

histogram = utils.get_equalized_histogram(image)

utils.print_array_into_file('result.txt', histogram)

utils.show_histogram(histogram)