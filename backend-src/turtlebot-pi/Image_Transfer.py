# !/usr/bin/env python2
import Image_Server
import random
import socket, select
from time import gmtime, strftime
import os

def transfer_images():

    folder_name= "IndoorView_Images"
    save_location = "/home/pi/Desktop/"+ folder_name

    #Find the total number of images in the saved folder
    total_image_count= 0

    for file in os.listdir(save_location):
            if file.endswith('.jpg'):
                    #print(file)
                    total_image_count = total_image_count + 1
                    
    print "Total image count detected: " + str(total_image_count)
    count = 1
    while (count <= total_image_count):
        pic = save_location + "/" + 'image_' + str(count) + '.jpg'
        picID = 'image_' + str(count)
        print '%s is being processed' % picID
        Image_Server.transfer(pic)
        count = count +1

