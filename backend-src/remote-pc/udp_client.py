# Save as client.py 
# Message Sender
import os
from socket import *
import time
import clientImage

def send_to_PI(host, message):
	#host = "192.168.0.11" #IP Address of Raspberry Pi
	port = 13000
	addr = (host, port)
	UDPSock = socket(AF_INET, SOCK_DGRAM)
	while True:
	    #data = raw_input("Enter message to send or type 'exit': ")
	    data = message
	    UDPSock.sendto(data, addr)
	    if data == "exit":
		break

	    elif data=="capture":
		(data,addr)=UDPSock.recvfrom(1024)
		#print data
		if data == "image_captured":
			return 1
			#return a boolean or variable to indicate capturing of image is complete
            elif data=="save_all_images":
                (data,addr)=UDPSock.recvfrom(1024)
                if data == "activate_receiver_client":
                        (data,addr)=UDPSock.recvfrom(1024)
                        image_count = int(data)
                        print image_count
                        #Activate client.py
                        time.sleep(2)
                        print 'execute clientImage'
                        clientImage.client(image_count)
                        #execfile('clientImage.py')

                (data,addr)=UDPSock.recvfrom(1024)
		#print data
		if data == "images_transferred":
			return 1
			#return a boolean or variable to indicate capturing of image is complete






	UDPSock.close()
	os._exit(0)

