# !/usr/bin/env python2

import random
import socket, select
from time import gmtime, strftime
import netifaces as ni

def transfer(current_image):
    HOST = ni.ifaddresses('wlan0')[ni.AF_INET][0]['addr']
    PORT = 6666
    cnt = 0
    connected_clients_sockets = []
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(10)
    connected_clients_sockets.append(server_socket)
    
    def recvall(sock, msgLen):
        msg = ""
        bytesRcvd = 0

        while bytesRcvd < msgLen:
            chunk = sock.recv(msgLen - bytesRcvd)

            if chunk == "": break
            bytesRcvd += len(chunk)
            msg += chunk

            if "\r\n" in msg: break
        return msg


    while True:
        if cnt == 1:
            break
        read_sockets, write_sockets, error_sockets = select.select(connected_clients_sockets, [], [])

        for sock in read_sockets:
            if sock == server_socket:
                sockfd, client_address = server_socket.accept()
                connected_clients_sockets.append(sockfd)

            else:
                try:
                    data = recvall(sock, 4096)

                    if data:
                        txt = data.strip()

                        if txt == 'Receive':
                            sock.sendall('Ok\r\n')

                        elif txt == 'Size':
                            with open(current_image, 'rb') as f:
                                file_size = len(f1.read())
                                f.seek(0)

                            file_size = '%s' % file_size
                            sock.sendall('Size %s\r\n' % file_size)

                        elif txt == 'image_data':
                            with open(current_image, 'rb') as f2:
                                image_data = f2.read()
                            msg = '%send_of_image\r\n' % image_data
                            sock.sendall(msg)

                        elif txt == 'Finished':
                            sock.close()
                            connected_clients_sockets.remove(sock)
                            cnt = cnt + 1
                except:
                    sock.close()
                    connected_clients_sockets.remove(sock)
                    continue
    server_socket.close()

