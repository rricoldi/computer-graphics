import numpy as np
import cv2 as cv 
import matplotlib.pyplot as plot
import math
import os

def get_matrix_of_zeros(width, height):
  return np.zeros((width, height))

def get_alpha(u, n):
  if u == 0:
    return math.sqrt(1/n)
  else:
    return math.sqrt(2/n)

def get_cos(x, u, n):
  z = (2*x + 1)*u*math.pi
  return math.cos(z/(2*n))


def get_normalized_value(number: float):
  return number/255

def get_dct_by_u_v(u, v, n, m, image):
  alpha_u = get_alpha(u,  n)
  alpha_v = get_alpha(v,  m)
  aux_sum = 0
  for x in range(n):
    for y in range(m):
      value = image[x][y]
      aux_sum += (value * get_cos(x, u, n) * get_cos(y, v, m))

  return alpha_u * alpha_v * aux_sum

def get_bi_dimensional_dct_by_image(image):
  height, width = image.shape
  dct_image = get_matrix_of_zeros(height, width)
  counter = 0
  for u in range(height):
    print('{:.2f}%'.format((counter*100)/(height*width)))
    for v in range(width):
      counter += 1
      dct_image[u][v]= get_dct_by_u_v(u, v, height, width, image)

  return dct_image

def get_pixel_by_u_v(x, y, n, m, image):
  aux_sum = 0
  for u in range(n):
    for v in range(m):
      alpha_u = get_alpha(u,  n)
      alpha_v = get_alpha(v,  m)
      value = image[u][v]
      aux_sum += (alpha_u * alpha_v * value * get_cos(x, u, n) * get_cos(y, v, m))

  return aux_sum


def get_image_by_bi_dimensional_dct(dct_matrix):
  height = len(dct_matrix)
  width = len(dct_matrix[0])
  image = get_matrix_of_zeros(height, width)

  for x in range(height):
    for y in range(width):
      image[x][y]= get_pixel_by_u_v(x, y, height, width, dct_matrix)

  return image

def get_distance_from_init(x, y):
  return math.sqrt((math.pow(x, 2) + math.pow(y, 2)))

def fpbi(x, y, d0):
  if(get_distance_from_init(x, y) <= d0):
    return 1
  else:
    return 0

def fpai(x, y, d0):
  if(get_distance_from_init(x, y) <= d0):
    return 0
  else:
    return 1


def get_filtered_matrix(filter_function, image, d0):
  height = len(image)
  width = len(image[0])
  filter = get_matrix_of_zeros(height, width)

  for x in range(height):
    for y in range(width):
      filter[x][y] = filter_function(x, y, d0)

  return filter

def get_image_filtered(image, filtered_frequency):
  return image * filtered_frequency


def print_matrix_into_file(textFilePath, matrix):
  if os.path.exists(textFilePath):
    os.remove(textFilePath)

  textFile = open(textFilePath, 'x')
  for row in range(len(matrix)):
    for column in range(len(matrix[0])):
      textFile.write('{:.2f}, '.format(matrix[row][column]))
    textFile.write('\n')