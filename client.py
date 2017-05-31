# This will be an other pool of methods and classes for all clients -> classroomservers and smartdesks
import threading
import time


class Command_Executer:
    def __init__(self):
        pass

    def execute(command):
        pass


class CommandListener(threading.Thread):       # This class allows you to Listen on a port for Networktraffic which will be transfered to the Command_Executer
    def __init__(self, threadID, name, listening_port):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.listening_port

    def run(self):
        base.running_threads.append(self.name)
        while True:
            command = base.NetworkManager.listen(self.listening_port)   # This will maybe cause errors if 2 clients send something at the same time. This is something I need to time an other time
            Command_Executer.execute(command)
