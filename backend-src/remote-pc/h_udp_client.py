import udp_client
import sys

#HIGH-LEVEL UDP CLIENT


#def hUDPClient():
command = raw_input("Enter_command:")
RASPBERRY_PI_IP = "172.17.7.6"

#If a = 1 this means command was successful

if command == "capture":
    a = udp_client.send_to_PI(RASPBERRY_PI_IP,"capture")
    if a:
        print "Image Captured"
    else:
        print "Failed to Capture"
        
elif command == "save_all_images":
    a = udp_client.send_to_PI(RASPBERRY_PI_IP,"save_all_images")
    if a:
        print "Message Received"
    else:
        print "Failed to Receive"
else:
    print "Not a valid command"
    exit()
