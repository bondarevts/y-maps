#!/usr/bin/env python3
from PIL import Image
import os

IMAGE_SIZE = 256


def create_image(source_dir, x_from, x_to, y_from, y_to, filename):
    width = IMAGE_SIZE * (x_to - x_from + 1)
    height = IMAGE_SIZE * (y_to - y_from + 1)

    print('create picture')
    result = Image.new('RGB', (width, height))
    print('Picture created')
    y = 0
    for j in range(y_from, y_to + 1):
        x = 0
        for i in range(x_from, x_to + 1):
            image_name = os.path.join(source_dir, 'm' + str(i) + 'x' + str(j) + '.png')
            result.paste(Image.open(image_name), (x, y))
            x += IMAGE_SIZE
        y += IMAGE_SIZE

    print('save image in file')
    result.save(filename)
    print('saved in ' + filename)


def create_map(source_dir, result_dir, start_x, end_x, start_y, end_y):
    print('range x: ' + str(end_x - start_x + 1) + ' y: ' + str(end_y - start_y + 1))
    create_image(source_dir, start_x, end_x, start_y, end_y, os.path.join(result_dir, 'full.png'))


def create_advanced_map(source_dir, result_dir, start_x, end_x, start_y, end_y, width_step, height_step, crossover):
    x = start_x
    xi = 0
    while x < end_x:
        x = max(x - crossover, start_x)
        yi = 0
        y = start_y
        while y < end_y:
            y = max(y - crossover, start_y)
            create_image(source_dir, x, min(x + width_step - 1, end_x), y, min(y + height_step - 1, end_y),
                         os.path.join(result_dir, 'map_x' + str(xi) + 'y' + str(yi) + '.png'))
            y += height_step
            yi += 1
        x += width_step
        xi += 1


# create_advanced_map('/home/tim/maps/', '/home/tim/results/', 737, 769, 373, 399)
create_advanced_map(source_dir='/home/tim/full_map/', result_dir='/home/tim/results_1/',
                    start_x=679, end_x=816, start_y=298, end_y=469,
                    width_step=34,  height_step=24, crossover=1)
