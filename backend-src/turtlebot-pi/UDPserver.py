# Save as server.py
# Message Receiver
import os
from socket import *
import time
# Must import the python script to call the capture image function
#import imageCapture
# Must import the python script to transfer images
import test
# Import Image Couter (Sends total image amount to Remote-PC)
import imageCounter
from subprocess import call

# host = "192.168.0.11" #IP Address of Raspberry Pi
host = "172.17.29.22"
port = 13000
buf = 1024
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.bind(addr)
print "Waiting to receive message..."
while True:
    (data, addr) = UDPSock.recvfrom(buf)
    print "Received message: " + data
    # When message received is 'exit_server' this script will terminate
    if data == "exit_server":
        break
    elif data == "capture":
        print "Capturing IMAGE...(in progress)"
        # Call the Capture Image Python Script to Capture a single 360 image
        # imageCapture.capture()
        #call("python3 imageCapture.py")
        os.system('python3 imageCapture.py')
        time.sleep(2)  # Simulates Image Capture

        print "Sent Confirmation to Remote-PC"
        data = "image_captured"
        UDPSock.sendto(data, addr)
        print "---- Capture Complete ----"
        print ""
        print "Waiting to receive next message..."
    elif data == "save_all_images":
        print "SAVING ALL IMAGES to REMOTE PC...(in progress)"

        print "Activate RECEIVER CLIENT"
        total_image_count = imageCounter.count()
        data = "activate_receiver_client"
        UDPSock.sendto(data, addr)
        time.sleep(0.5)
        data = str(total_image_count)
        UDPSock.sendto(data, addr)

        # Call the script to initiate the Image Transfer System
        test.imageTransfer()
        # time.sleep(5) # Simulates Image Transfer

        print "Sent Confirmation to Remote-PC"
        data = "images_transferred"
        UDPSock.sendto(data, addr)
        print "---- Sequence Complete ----"
        print ""
        print "Waiting to receive next message..."
UDPSock.close()
os._exit(0)
