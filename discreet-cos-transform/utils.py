import numpy as np
import cv2 as cv 
import matplotlib.pyplot as plot
import math
import os

def get_matrix_of_zeros(width, height):
  return np.zeros((width, height))

# def get_histogram(image):
#   height, width = image.shape

#   histogram = get_array_of_zeros(256)

#   for column in range(height):
#     for row in range(width):
#       intensity = image[column, row]

#       histogram[intensity] += 1

#   return histogram

def get_alpha(u, n):
  if u == 0:
    return math.sqrt(1/n)
  else:
    return math.sqrt(2/n)

def get_cos(x, u, n):
  z = (2*x + 1)*u*math.pi
  return math.cos(z/(2*n))

# def get_dct_by_u(u, n, histogram):
#   alpha = get_alpha(u,  n)
#   aux_sum = 0
#   for x in range(n-1):
#     aux_sum += (histogram[x] * get_cos(x, u, n))
  
#   return alpha * aux_sum

# def get_dct_by_histogram(histogram, n):
#   dct_histogram = get_array_of_zeros(n)
#   for u in range(n-1):
#     dct_histogram[u] = get_dct_by_u(u, n, histogram)

#   return dct_histogram

# def show_histogram(histogram, name):
#   plot.title(name)
#   plot.plot(histogram)
#   plot.xlabel('X')
#   plot.ylabel('Y')
#   plot.show()

# def print_array_into_file(textFilePath, array):
#   if os.path.exists(textFilePath):
#     os.remove(textFilePath)

#   textFile = open(textFilePath, 'x')
#   counter = 0
#   for row in range(len(array)):
#     counter += array[row]
#     textFile.write('{} - {} '.format(row, array[row]))
#     textFile.write('\n')
#   textFile.write('{} px'.format(counter))

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
  dct_image = get_matrix_of_zeros(width, height)

  for u in range(width):
    for v in range(height):
      dct_image[u][v]= get_dct_by_u_v(u, v, width, height, image)

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
  image = get_matrix_of_zeros(width, height)

  for x in range(width):
    for y in range(height):
      image[x][y]= get_pixel_by_u_v(x, y, width, height, dct_matrix)

  return image

def print_matrix_into_file(textFilePath, matrix):
  if os.path.exists(textFilePath):
    os.remove(textFilePath)

  textFile = open(textFilePath, 'x')
  for row in range(len(matrix)):
    for column in range(len(matrix[0])):
      textFile.write('{:.2f}, '.format(matrix[row][column]))
    textFile.write('\n')