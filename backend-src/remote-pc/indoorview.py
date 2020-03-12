import cmd
import os
from mappoints import MapPoints
import StartRVIZ
import subprocess
import rospy
from threading import Thread
from savetodatabase import Database


class IndoorViewShell(cmd.Cmd):
    intro = "Welcome to the IndoorView data collection software system. Type help or ? to list commands\n"
    prompt = "(indoorView) "
    file = NotImplemented

    def __init__(self):
        self.map_created = False
        self.map_saved = False
        self.localization_performed = False
        self.database = Database()
        cmd.Cmd.__init__(self)

    def do_create_map(self, arg):
        "Map an area for indoorView with map name as argument"
        StartRVIZ.start_rviz()
        subprocess.Popen(
            ["rostopic pub /reset std_msgs/Empty \"{}\""], shell=True, stdout=subprocess.PIPE)
        rospy.init_node('listener', anonymous=True)
        self.mappoints = MapPoints(arg)
        rospy.loginfo("Please click points of interest on map in order!")
        rospy.loginfo("Run save_map when done")
        listen = Thread(target=self.mappoints.listener, args=())
        listen.daemon = True
        listen.start()
        self.map_created = True
        return

    def do_save_map(self, arg):
        "Save map to maps folder with map name specified when creating map.\nMust be called after create_map"
        if self.map_created:
            self.mappoints.check_for_done()
            self.map_saved = True
        else:
            print("Please run create_map <map name> first")

    def do_perform_localization(self, arg):
        "Localize TurtleBot in the previously saved map.\n Must be called after save_map"
        if self.map_saved:
            self.mappoints.perform_localization()
            self.localization_performed = True
        else:
            print("Please run save_map first")

    def do_perform_navigation(self, arg):
        "Autonomously capture images at saved points in order"
        if self.localization_performed:
            self.mappoints.perform_navigation()
        else:
            print("Please run perform_localization first")

    def do_get_maps(self, arg):
        "Get list of maps saved on the database"
        maps = self.database.get_maps()
        for map in maps:
            print(str(map[0]) + " " + str(map[1]))

    def do_delete_map(self, arg):
        "Delete map from database"
        self.database.delete_map(arg)

    def do_shut_down(self, arg):
        "Shut down system"
        os.system("gnome-terminal -x rosnode kill -a")
        exit()


def parse(arg):
    return tuple(map(arg.split()))


if __name__ == "__main__":
    IndoorViewShell().cmdloop()
