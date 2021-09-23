import numpy as np
import cv2 as cv 
import math
import os

def normalize_rgb_values_to_interval_0_1(number: float):
  return number/255

def get_normalized_rgb_values(r: int, g: int, b: int):
  return [
    normalize_rgb_values_to_interval_0_1(r),
    normalize_rgb_values_to_interval_0_1(g),
    normalize_rgb_values_to_interval_0_1(b)
  ]

def get_intensity_by_rgb(r: float, g: float, b: float):
  return float((r+g+b)/3)

def get_saturation_by_rgb(r: float, g: float, b: float):
  rgb_summed_values = r + g + b

  if rgb_summed_values == 0:
    return 1

  min_rgb_value = min([r, g, b])

  return 1 - ((3/rgb_summed_values) * min_rgb_value)

def get_hue_angle_by_rgb(r: float, g: float, b: float):
  divider = math.sqrt((r - g)**2 + ((r - b) * (g - b)))

  if divider == 0:
    return 0

  dividend = ((r - g) + (r - b)) / 2

  return math.acos(dividend/divider)

def get_hue_by_rgb(r: float, g: float, b: float):
  if b <= g:
    return get_hue_angle_by_rgb(r, g, b)
  else:
    return 360 - get_hue_angle_by_rgb(r, g, b)

def get_hsi_pixel_by_rgb_pixel(r: float, g: float, b: float):
  return [
    get_hue_by_rgb(r, g, b),
    get_saturation_by_rgb(r, g, b),
    get_intensity_by_rgb(r, g, b),
  ]

def get_hsi_by_rgb(r_matrix: int, g_matrix: int, b_matrix: int):
  [r_matrix, g_matrix, b_matrix] = get_normalized_rgb_values(r_matrix, g_matrix, b_matrix)

  hsi_matrix = cv.merge([r_matrix, g_matrix, b_matrix])

  for row in range(len(r_matrix)):
    for column in range(len(r_matrix[0])):
      hsi_matrix[row][column] = get_hsi_pixel_by_rgb_pixel(
        r_matrix[row][column], 
        g_matrix[row][column], 
        b_matrix[row][column]
      )

  return hsi_matrix

def print_matrix_into_file(textFilePath, matrix: float):
  if os.path.exists(textFilePath):
    os.remove(textFilePath)

  textFile = open(textFilePath, 'x')

  for row in range(len(matrix)):
    for column in range(len(matrix[0])):
      for thirdDimension in range(len(matrix[0][0])):
        textFile.write('{:.2f} '.format(matrix[row][column][thirdDimension]))
      textFile.write(' | ')
    textFile.write('\n')