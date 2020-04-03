# Message Receiver
import socket
import sys
import os
import time
#Must import the python script to transfer images
import test
#Import Image Counter (Sends total image amount to Remote-PC)
import imageCounter
from subprocess import call
import netifaces as ni

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ni.ifaddresses('wlan0')[ni.AF_INET][0]['addr']
# Bind the socket to the port
server_address = (host, 10000)
print >>sys.stderr, 'Starting up Server... %s port %s' % server_address
sock.bind(server_address)

print "Waiting to receive message..."
# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()

    try:
        print >>sys.stderr, ''
        print >>sys.stderr, '===================================='
        print >>sys.stderr, 'Connection from:', client_address

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            print >>sys.stderr, 'Received "%s"' % data
            if data:
                print >>sys.stderr, 'Sending data back to the client'
                connection.sendall(data)
                print >>sys.stderr, '123'

                #When message received is 'exit_server' this script will terminate
                if data == "capture":
                    print "Capturing IMAGE...(in progress)"
                    #Call the Capture Image Python Script to Capture a single 360 image
                    #imageCapture.capture()
                    #call("python3 imageCapture.py")
                    os.system('python3 imageCapture.py')
                    time.sleep(2) # Simulates Image Capture

                    print "Sent Confirmation to Remote-PC"
                    data = "image_captured"
                    connection.sendall(data)
                    print "---- Capture Complete ----"
                    print ""
                    print "Waiting to receive next message..."
                elif data == "save_all_images":
                    print "SAVING ALL IMAGES to REMOTE PC...(in progress)"
                    os.system('python3 imageRename.py')
                    time.sleep(1)
                    print "Activate RECEIVER CLIENT"
                    total_image_count = imageCounter.count()
                    print (total_image_count)
                    #total_image_count = 3
                    data = "activate_receiver_client"
                    connection.sendall(data)
                    time.sleep(0.5)
                    data = str(total_image_count)
                    connection.sendall(data)
                    
                    #Call the script to initiate the Image Transfer System
                    test.imageTransfer()
                    
                    #time.sleep(5) # Simulates Image Transfer

                    print "Sent Confirmation to Remote-PC"
                    data = "images_transferred"
                    connection.sendall(data)
                    print "---- Sequence Complete ----"
                    print ""
                    print "Waiting to receive next message..."



            else:
                print >>sys.stderr, 'No more data from', client_address
                break
            
    finally:
        # Clean up the connection
        print >>sys.stderr, 'Connection close...'
        print >>sys.stderr, ''
        connection.close()