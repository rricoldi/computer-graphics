import numpy as np
import math

def normalize_rgb_values_to_interval_0_1(number: float):
  return number/255

def get_normalized_rgb_values(r: int, g: int, b: int):
  return [
    normalize_rgb_values_to_interval_0_1(r),
    normalize_rgb_values_to_interval_0_1(g),
    normalize_rgb_values_to_interval_0_1(b)
  ]

def get_intensity_by_rgb(r: int, g: int, b: int):
  return float((r+g+b)/3)

def get_saturation_by_rgb(r: int, g: int, b: int):
  min_rgb_value = min([r, g, b])
  rgb_summed_values = r + g + b

  return 1 - (float(3/rgb_summed_values) * min_rgb_value)

def get_hue_angle_by_rgb(r: int, g: int, b: int):
  dividend = ((r - g) + (r - b)) / 2
  divider = math.sqrt(math.pow(r-g, 2) + ((r-b)*(g-b)))

  return math.acos(dividend/divider)

def get_hue_by_rgb(r: int, g: int, b: int):
  if b <= g:
    return get_hue_angle_by_rgb(r, g, b)
  else:
    return 360 - get_hue_angle_by_rgb(r, g, b)

def get_hsi_by_rgb(r: int, g: int, b: int):
  [r, g, b] = get_normalized_rgb_values(r, g, b)

  return [
    get_hue_by_rgb(r, g, b),
    get_saturation_by_rgb(r, g, b),
    get_intensity_by_rgb(r, g, b),
  ]