
import numpy as np
from PIL import Image
import io
import math

# '../../frontend-webapp/maps/LocalizationTestMap.pgm'


def convert_file_to_array(image_path):
    with open(image_path, 'r') as file:
        lines = file.readlines()

    # Ensure file is appropriate format
    if (lines[0] != 'P5\n'):
        print("Error: File is not binary encoded pgm!")
        exit()

    # Get file dimensions in pixels from header
    x_max_str, y_max_str = lines[2].split()
    x_max = int(x_max_str)
    y_max = int(y_max_str)

    if (lines[3] != '255\n'):
        print("Error: pgm encoding is not 8-bit!")

    # Preallocate array to hold image data
    # Numbers are 8-bit but use 32 bits bc python keeps type after operation
    map = np.zeros((y_max, x_max), dtype=np.uint32)
    for y in range(0, y_max):
        for x in range(0, x_max):
            map[y][x] = int(repr((lines[4][y * y_max + x]))[3:5], 16)

    return map


def convert_ImageObj_array(image, size):
    x_max = int(size[0])
    y_max = int(size[1])

    # Preallocate array to hold image data
    # Numbers are 8-bit but use 32 bits bc python keeps type after operation
    map = np.zeros((y_max, x_max), dtype=np.uint32)
    for y in range(0, y_max):
        for x in range(0, x_max):
            map[y][x] = image.getpixel((x, y))

    return map


def perform_matching(map, template):
    x_map = len(map[0])
    y_map = len(map)

    x_template = len(template[0])
    y_template = len(template)

    x_result = x_map - x_template
    y_result = y_map - y_template

    result = np.zeros((x_result, y_result))

    max_result = 0
    max_result_x = int()
    max_result_y = int()

    for y in range(0, y_result):
        for x in range(0, x_result):
            Sum_T_I = 0
            Sum_T2 = 0
            Sum_I2 = 0
            # Iterate over image result
            for y_ in range(0, y_template):
                for x_ in range(0, x_template):
                    Sum_T_I += (template[y_][x_] * map[y + y_][x + x_])
                    Sum_T2 += template[y_][x_]**2
                    Sum_I2 += map[y + y_][x + x_]**2

            result[y][x] = Sum_T_I/math.sqrt(Sum_T2 * Sum_I2)
            if result[y][x] > max_result:
                max_result = result[y][x]
                max_result_x = x
                max_result_y = y

    print(result)
    print("Max Result: " + str(max_result))
    print("X: " + str(max_result_x))
    print("Y: " + str(max_result_y))


map = convert_file_to_array(
    '../../frontend-webapp/maps/LocalizationTestMap.pgm')

with open('../../frontend-webapp/maps/LocalizationTestMap.pgm', 'r') as file:
    lines = file.readlines()
size = lines[2].split()
image = Image.open('../../frontend-webapp/maps/LocalizationTestMap.pgm')
image_cropped = image.crop((80, 80, 160, 160))
template = convert_ImageObj_array(image_cropped, ('80', '80'))

perform_matching(map, template)
