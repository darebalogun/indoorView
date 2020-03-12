import tcp_message_client
import sys

# HIGH-LEVEL TCP CLIENT

def send(command, map_name):
    #command = raw_input("Enter_command:")
    RASPBERRY_PI_IP = "172.17.29.22"

    # If a = 1 this means command was successful

    if command == "capture":
        a = tcp_message_client.send_to_PI(RASPBERRY_PI_IP, "capture", map_name)
        if a:
            print "Image Captured"
        else:
            print "Failure to Capture Image"

    elif command == "save_all_images":
        a = tcp_message_client.send_to_PI(RASPBERRY_PI_IP, "save_all_images", map_name)
        if a:
            print "Message Received - Image Successfully Transferred"
        else:
            print "Failed to Transfer Images"
    else:
        print "Not a valid command"
        exit()
