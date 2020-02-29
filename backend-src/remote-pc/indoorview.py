import cmd
from mappoints import MapPoints
import StartRVIZ
import subprocess
import rospy
from threading import Thread


class IndoorViewShell(cmd.Cmd):
    intro = "Welcome to the IndoorView data collection software system. Type help or ? to list commands\n"
    prompt = "(indoorView) "
    file = NotImplemented

    def do_create_map(self, arg):
        "Map an area for indoorView with map name as argument"
        StartRVIZ.start_rviz()
        subprocess.Popen(
            ["rostopic pub /reset std_msgs/Empty \"{}\""], shell=True, stdout=subprocess.PIPE)
        rospy.init_node('listener', anonymous=True)
        self.mappoints = MapPoints(arg)
        listen = Thread(target=self.mappoints.listener, args=())
        listen.daemon = True
        listen.start()

    def do_save_map(self, arg):
        "Save map to maps folder with map name specified when creating map.\nMust be called after create_map"
        self.mappoints.check_for_done()


def parse(arg):
    return tuple(map(arg.split()))


if __name__ == "__main__":
    IndoorViewShell().cmdloop()
