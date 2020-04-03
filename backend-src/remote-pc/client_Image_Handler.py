#!/usr/bin/env python

import socket
import sys
import time
import os
import shutil


def receive(image_count, map_name):
    cc = 1

    image_folder = "../../frontend-webapp/images/" + map_name

    if not os.path.exists(image_folder):
        os.mkdir(image_folder)
    else:
        shutil.rmtree(image_folder)
        os.mkdir(image_folder)

    while (cc <= image_count):
        # server IP:
        HOST = '172.17.29.22'
        PORT = 6666

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = (HOST, PORT)
        sock.connect(server_address)

        fname = '../../frontend-webapp/images/' + \
            map_name + '/image' + str(cc) + '.jpg'

        def recvall(sock, msgLen):
            msg = ""
            bytesRcvd = 0

            while bytesRcvd < msgLen:

                chunk = sock.recv(msgLen - bytesRcvd)

                if chunk == "":
                    break

                bytesRcvd += len(chunk)
                msg += chunk

                if "\r\n" in msg:
                    break
            return msg

        try:

            sock.sendall("Receive\r\n")
            data = recvall(sock, 4096)

            if data:
                txt = data.strip()

                if txt == 'Ok':

                    sock.sendall("Size\r\n")
                    data = recvall(sock, 4096)

                    if data:
                        txt = data.strip()

                        if txt.startswith('Size'):
                            
                            tmp = txt.split()
                            size = int(tmp[1])

                            sock.sendall("image_data\r\n")

                            myfile = open(fname, 'wb')
                            amount_received = 0
                            while amount_received < size:
                                data = recvall(sock, 4096)
                                if not data:
                                    break
                                amount_received += len(data)

                                #print "Amount of Data received: %s" %amount_received
                                txt = data.strip('\r\n')

                                if 'end_of_image' in str(txt):
                                    print 'Image received successfully'
                                    cc = cc+1
                                    myfile.write(data)
                                    myfile.close()
                                    sock.sendall("Finished\r\n")
                                    time.sleep(3)
                                    break
                                    sock.close
                                else:
                                    myfile.write(data)
        finally:
            sock.close()
