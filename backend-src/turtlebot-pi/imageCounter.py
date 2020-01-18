import os


def count():
    folder_name= "IndoorView_Images"
    save_location = "/home/pi/Desktop/"+ folder_name

    #Find the total number of images in the saved folder
    total_image_count= 0

    for file in os.listdir(save_location):
            if file.endswith('.jpg'):
                    #print(file)
                    total_image_count = total_image_count + 1
                    
    print "Images that should be received: " + str(total_image_count)
    
    return total_image_count