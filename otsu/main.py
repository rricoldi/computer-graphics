import cv2 as cv 
import sys
import numpy as np
import utils

image = cv.imread(sys.argv[1]) 

b, g, r = cv.split(image)
cv.imwrite('red-band.jpg', r)

height, width = image.shape[:2]

# Passo 1: tratar o histograma como uma função de probabilidade
histogram = utils.get_histogram(r, width, height)
normalized_histogram = utils.get_normalized_histogram(histogram, width*height)

# Aplica Otsu para descobrir o Limiar com maior variância
# Os outros 7 passos estão nesta função
t = utils.otsu(normalized_histogram, 256)
print('O limiar usado foi:', t)

# Aplica o limiar na banda da imagem
thresholded_band = utils.apply_thresholding(b, t)

cv.imwrite('thresholded-image.jpg', thresholded_band)