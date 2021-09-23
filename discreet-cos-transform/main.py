import cv2 as cv 
import sys
import numpy as np
import utils

image = cv.imread(sys.argv[1]) 

b, g, r = cv.split(image)

# histogram = utils.get_histogram(b)
# dct_histogram = utils.get_dct_by_histogram(histogram, 256)

# utils.print_array_into_file('result.txt', histogram)
# utils.print_array_into_file('result-dct.txt', dct_histogram)

# utils.show_histogram(histogram, 'Histogram')
# utils.show_histogram(dct_histogram, 'DCT')
utils.print_matrix_into_file('image.txt', b)

dct_matrix = utils.get_bi_dimensional_dct_by_image(b)
dct_image = utils.get_image_by_bi_dimensional_dct(dct_matrix)
utils.print_matrix_into_file('result.txt', dct_image)
cv.imwrite('blue.jpg', b)
cv.imwrite('result.jpg', dct_image)