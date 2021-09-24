import cv2 as cv 
import sys
import numpy as np
import utils

image = cv.imread(sys.argv[1]) 

b, g, r = cv.split(image)

utils.print_matrix_into_file('image.txt', b)

dct_matrix = utils.get_bi_dimensional_dct_by_image(b)
image_filter = utils.get_filtered_matrix(utils.fpbi, dct_matrix, 18)
filtered_frequency = utils.get_image_filtered(dct_matrix, image_filter)
fpbi_image = utils.get_image_by_bi_dimensional_dct(filtered_frequency)

image_filter = utils.get_filtered_matrix(utils.fpai, dct_matrix, 18)
filtered_frequency = utils.get_image_filtered(dct_matrix, image_filter)
fpai_image = utils.get_image_by_bi_dimensional_dct(filtered_frequency)


cv.imwrite('blue-band.jpg', b)
cv.imwrite('filtered-with-fpbi-image.jpg', fpbi_image)
cv.imwrite('filtered-with-fpai-image.jpg', fpai_image)