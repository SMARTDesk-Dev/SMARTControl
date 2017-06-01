# This will be an other pool of methods and classes for all clients -> classroomservers and smartdesks
from subprocess import call
import base
import threading
import time


class Command_Executer:
    def __init__(self):
        pass

    def execute(command, stop_method):
        if command is "0000":
            call(["shutdown", "-h", "now"])
        elif command is "0001":
            call(["shutdown", "-r", "now"])
        elif command is "0002":
            call([""])                              # Log off -> Send Greeter message to restart
        elif command is "0003":                     # Everything down here for more commands
            pass


class CommandListener(threading.Thread):       # This class allows you to Listen on a port for Networktraffic which will be transfered to the Command_Executer
    def __init__(self, threadID, name, listening_port):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.listening_port

    def stop(self):
        self._stop_event.set()
        base.running_threads.remove(self.name)

    def stopped(self):
        return self._stop_event.is_set()

    def run(self):
        base.running_threads.append(self.name)
        while True:
            command = base.NetworkManager.listen(self.listening_port)
            Command_Executer.execute(command, stop_method)


def setup_client(config, key, device):      # initializes some useful stuff -> TODO: This method is not that clean written maybe I will change it later
    result = base.Database.send_query("SELECT ip, port FROM " + base.File_Loader.get_config_string(config[0], config[1], "table") + " WHERE type=\'mas\'"))
    self.master_ip_address = result[0]
    self.master_port = result[1]
    self.key = key
    self.device = device
    self.config = config

def refresher():            # Tells the master that a client is still alive
    base.NetworkManager.send_packet(master_ip_address, master_port, base.Crypter.encrypt(key, base.get_ip(base.File_Loader.get_config_string(config[0], config[2], "mac")) + base.get_mac(base.File_Loader.get_config_string(config[0], config[2], "ip")) + device)))
