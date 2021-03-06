from time import sleep
from datetime import datetime
from sh import gphoto2 as gp
import signal
import os
import subprocess


# kill gphoto2 process thatstarts whenever we connect the camera
def killgphoto2Process():
    p = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
    out, err = p.communicate()

    # search for the line that has the process we want to kill
    for line in out.splitlines():
        if b'gvfsd-gphoto2' in line:
            # kill the process
            pid = int(line.split(None, 1)[0])
            os.kill(pid, signal.SIGKILL)


shot_date = datetime.now().strftime("%Y-%m-%d")
shot_time = datetime.now().strftime("%Y-%m-%d %H:%M;%S")
picID = "PiShots"

clearCommand = ["--folder", "/store_00010001/DCIM/100RICOH/",
                "-R", "--delete-all-files"]
triggerCommand = ["--trigger-capture"]
downloadCommand = ["--get-all-files"]

#folder_name = shot_date + picID
#save_location = "/home/pi/Desktop/gphoto/images/"+ folder_name
folder_name = "IndoorView_Images"
save_location = "/home/pi/Desktop/" + folder_name


def createSaveFolder():
    try:
        os.makedirs(save_location)
    except:
        print("Failed to create the new directory.")
    os.chdir(save_location)


def captureImages():
    gp(triggerCommand)
    sleep(7)
    gp(downloadCommand)
    gp(clearCommand)


def renameFiles(ID):
    for filename in os.listdir("."):
        print(filename)
        if len(filename) < 13:
            if filename.endswith(".JPG"):
                os.rename(filename, (shot_time + ID + ".JPG"))
                print("Renamed the JPG")


killgphoto2Process()
gp(clearCommand)
createSaveFolder()
captureImages()
# renameFiles(picID)
