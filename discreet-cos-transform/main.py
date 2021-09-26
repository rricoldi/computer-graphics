import cv2 as cv 
import sys
import numpy as np
import utils

image = cv.imread(sys.argv[1]) 

b, g, r = cv.split(image)

d0 = int(input('Qual a distancia para o filtro passa baixa: '))
d1 = int(input('Qual a distancia para o filtro passa alta: '))

# imprime a banda que será utilizada para as filtragens e transformadas
cv.imwrite('blue-band.jpg', b)

# Pega a matriz no domínio da frequência aplicando a DCT bidimensional na imagem
dct_matrix = utils.get_bi_dimensional_dct_by_image(b)

# Aplica a DCT inversa retornando a imagem
decompressed_image = utils.get_image_by_bi_dimensional_dct(dct_matrix)

# Aplica o filtro na matriz de frequência
image_filter = utils.get_filtered_matrix(utils.fpbi, dct_matrix, d0)

# Faz a convolução do filtro Passa Baixa Ideal no espectro
filtered_frequency = utils.get_image_filtered(dct_matrix, image_filter)

# Aplica a DCT inversa retornando a imagem filtrada
fpbi_image = utils.get_image_by_bi_dimensional_dct(filtered_frequency)

# Aplica o filtro na matriz de frequência
image_filter = utils.get_filtered_matrix(utils.fpai, dct_matrix, d1)

# Faz a convolução do filtro Passa Alta Ideal no espectro
filtered_frequency = utils.get_image_filtered(dct_matrix, image_filter)

# Aplica a DCT inversa retornando a imagem filtrada
fpai_image = utils.get_image_by_bi_dimensional_dct(filtered_frequency)

# Aplica ruído na matriz de frequência
noisy_frequency = utils.generate_frequency_noise(dct_matrix)

# Aplica a DCT inversa retornando a imagem com ruído
noisy_image = utils.get_image_by_bi_dimensional_dct(noisy_frequency)

cv.imwrite('image-with-noise.jpg', noisy_image)
cv.imwrite('image-with-dct-and-inversed-dct.jpg', decompressed_image)
cv.imwrite('image-filtered-with-fpbi.jpg', fpbi_image)
cv.imwrite('image-filtered-with-fpai.jpg', fpai_image)