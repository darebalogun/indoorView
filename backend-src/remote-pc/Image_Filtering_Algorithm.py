#-------------------------------------------------------------------------------
# Name:        Image_Filtering_Algorithm
# Purpose:
#
# Author:      anannya
#
# Created:     13/03/2020
# Copyright:   (c) anannya 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from PIL import Image
import numpy

# Image_Filter - filtering images using median image processing
def Image_Filter(data, filter_size):
    # temporary array
    temp = []
    # adjusting whole number (filter_size) to the left of the number line
    indexer = filter_size // 2
    #indexing the image in the window
    Index_Window = [
        (m, n)
        for m in range(-indexer, filter_size-indexer)
        for n in range(-indexer, filter_size-indexer)
    ]
    # manipulating the pixels of the image and finding there mean
    Pixel_indexing = len(Index_Window) // 2
    # constructing a 2D array of pixels in image
    for m in range(len(data)):
        for n in range(len(data[0])):
            # sorting the pixels according to the median value of nearby pixels
            data[m][n] = sorted(
                0 if (
                    min(m+i, n+j) < 0
                    or len(data) <= m+i
                    or len(data[0]) <= n+j
                ) else data[m+i][n+j]

                for i , j in Index_Window

            )[Pixel_indexing ]
    return data

def main():
    img1 = Image.open("C:\\Users\\anann\\Desktop\\image_test\\initialpose.png").convert(
        "L")
    print(img1)
    arr = numpy.array(img1)
    # removed noise stores the image after filtering
    # filter_size = 3 can be changed to 5, 6, etc
    removed_noise = Image_Filter(arr, 3)
    # img1 consists the filtered image
    img2 = Image.fromarray(removed_noise)
    img2.show()

main()

