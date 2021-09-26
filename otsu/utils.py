import numpy as np
import cv2 as cv 
import matplotlib.pyplot as plot
import math
import os

def get_array_of_zeros(n):
  return [0] * n

def get_normalized_histogram(histogram, number_of_pixels: int):
  arr = get_array_of_zeros(256)

  for row in range(len(arr)):
    arr[row] = histogram[row] / number_of_pixels

  return arr

def get_histogram(band, width, height):
  histogram = get_array_of_zeros(256)

  for column in range(height):
    for row in range(width):
      intensity = band[column, row]

      histogram[intensity] += 1

  return histogram

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
    textFile.write('T = {}: {} '.format(row, array[row]))
    textFile.write('\n')

def get_avg_intensity_of_class_pixels(init, end, probability, histogram):
  if(probability == 0):
    return 0

  sum = 0

  for i in range(init, end):
    sum += i*histogram[i]

  return (1/probability)*sum

def otsu(normalized_histogram, l):
  biggest_threshold_variance = 0
  t = 0

  # Passo 2: Escolhe valores para T de 1 a L
  for threshold in range(1, l):
    # Passo 3: calcula as probabilidades de um pixel pertencer a classe 1 | [0, T]
    p1 = sum(normalized_histogram[0:threshold+1])

    # Passo 4: Calcula as probabilidades de um pixel pertencer a classe 2 | 1 -P1
    p2 = 1 - p1

    # Passo 5: Calcula a intensidade média dos pixels da classe 1
    m1 = get_avg_intensity_of_class_pixels(0, threshold+1, p1, normalized_histogram)

    # Passo 6: Calcula a intensidade média dos pixels da classe 2
    m2 = get_avg_intensity_of_class_pixels(threshold+2, l-1, p2, normalized_histogram)

    # Passo 7: Calcula a intensidade média dos pixels geral
    mg = get_avg_intensity_of_class_pixels(0, l-1, 1, normalized_histogram)

    # Passo 8: Escolhe o limiar T tal que maximize a variância entre as classes
    threshold_variance = p1*pow(m1-mg, 2) + p2*pow(m2-mg, 2)

    if(biggest_threshold_variance < threshold_variance):
      biggest_threshold_variance = threshold_variance
      t = threshold
    
  return t

def apply_thresholding(band, t):
  height = len(band)
  width = len(band[0])

  for x in range(height):
    for y in range(width):
      if band[x][y] > t:
        band[x][y] = 255
      else:
        band[x][y] = 0

  return band