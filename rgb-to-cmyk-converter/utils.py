import numpy as np

def normalize_rgb_values_to_interval_0_1(number: float):
  return number/255

def get_normalized_rgb_values(r: int, g: int, b: int):
  return [
    normalize_rgb_values_to_interval_0_1(r),
    normalize_rgb_values_to_interval_0_1(g),
    normalize_rgb_values_to_interval_0_1(b)
  ]

def get_one_minus_value(value: float):
  return 1 - value

def get_cmy_by_normalized_rgb(r: float, g: float, b: float):
  return [
    get_one_minus_value(r),
    get_one_minus_value(g),
    get_one_minus_value(b)
  ]

def get_value_without_black(value: float, black: float):
  return (value-black)/(1-black)

def get_cmyk_pixel_by_cmy_pixel(c_pixel: float, m_pixel: float, y_pixel: float):
  k = min(c_pixel, m_pixel, y_pixel)

  return [
    get_value_without_black(c_pixel, k),
    get_value_without_black(m_pixel, k),
    get_value_without_black(y_pixel, k),
    k
  ]

def get_cmyk_by_cmy(c_matrix: float, m_matrix: float, y_matrix: float):
  k_matrix = np.matrix(c_matrix)
  for row in range(len(c_matrix)):
    for column in range(len(c_matrix[0])):
      [c_pixel, m_pixel, y_pixel, black_pixel] = get_cmyk_pixel_by_cmy_pixel(c_matrix[row, column], m_matrix[row, column], y_matrix[row, column])
      c_matrix[row, column] = c_pixel
      m_matrix[row, column] = m_pixel
      y_matrix[row, column] = y_pixel
      k_matrix[row, column] = black_pixel

  return [
    c_matrix,
    m_matrix,
    y_matrix,
    k_matrix
  ]

def get_cmyk_by_rgb(r: int, g: int, b: int):
  [r, g, b] = get_normalized_rgb_values(r, g, b)

  [c, m, y] = get_cmy_by_normalized_rgb(r, g, b)

  return get_cmyk_by_cmy(c, m, y)