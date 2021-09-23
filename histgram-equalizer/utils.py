import numpy as np
import cv2 as cv 
import matplotlib.pyplot as plot
import math
import os

def get_array_of_zeros():
  return [0] * 256

def get_intensity_by_rgb(r, g, b):
  return int((r+g+b)/3)

def get_calculated_histogram(image):
  height, width, color = image.shape

  grey_matrix = get_array_of_zeros()

  for column in range(height):
    for row in range(width):
      b, g, r = image[column, row]

      intensity = 0

      if r+g+b != 0:
        intensity = get_intensity_by_rgb(r, g, b)

      grey_matrix[intensity] += 1

  return grey_matrix

def get_normalized_histogram(histogram, number_of_pixels: int):
  arr = get_array_of_zeros()

  for row in range(len(arr)):
    arr[row] = histogram[row] / number_of_pixels

  return arr



def get_equalized_histogram(image):
  height, width = image.shape[:2]
  calculated_histogram = get_calculated_histogram(image)
  print(calculated_histogram)
  normalized_histogram = get_normalized_histogram(calculated_histogram, width * height)
  print(normalized_histogram)

  aux_array = get_array_of_zeros()
  equalized_histogram = get_array_of_zeros()

  for row in range(len(aux_array)):
    sum = 0
    for column in range(row):
      sum += normalized_histogram[column]
    aux_array[row] = sum

  for row in range(height):
    for column in range(width):
      b, g, r = image[row, column]

      intensity = get_intensity_by_rgb(r, g, b)

      intensity = 255 * aux_array[intensity]

      equalized_histogram[int(intensity)] += 1

  return equalized_histogram

def show_histogram(histogram, name):
  plot.title(name)
  plot.plot(histogram)
  plot.xlabel('X')
  plot.ylabel('Y')
  plot.show()

def print_array_into_file(textFilePath, array):
  if os.path.exists(textFilePath):
    os.remove(textFilePath)

  textFile = open(textFilePath, 'x')

  for row in range(len(array)):
    textFile.write('{} '.format(array[row]))
    textFile.write('\n')