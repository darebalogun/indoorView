import socket
import sys
import os
import time
import client_Image_Handler


def send_to_PI(host, message, map_name):
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = (host, 10000)
    print >>sys.stderr, 'Connecting to %s port %s' % server_address
    sock.connect(server_address)

    try:
        
        # Send data
        #message = 'capture'
        print >>sys.stderr, 'sending "%s"' % message
        sock.sendall(message)

        # Look for the response
        amount_received = 0
        amount_expected = len(message)
        while amount_received < amount_expected:
            data = sock.recv(15)
            amount_received += len(data)
            print >>sys.stderr, 'Echo Command: "%s"' % data


        if message == "capture":
            data = sock.recv(16)

            #print data
            if data == "image_captured":
                return 1
                # return a boolean or variable to indicate capturing of image is complete

        elif message == "save_all_images":
            data = sock.recv(24)
            if data == "activate_receiver_client":
                data = sock.recv(1)
                image_count = int(data)
                print image_count
                # Activate client.py
                time.sleep(2)
                print 'execute clientImage'
                client_Image_Handler.receive(image_count, map_name)
                

            data = sock.recv(18)
            #print data
            if data == "images_transferred":
                return 1
                # return a boolean or variable to indicate capturing of image is complete


    finally:
        print >>sys.stderr, '----- Closing socket -----'
        sock.close()

