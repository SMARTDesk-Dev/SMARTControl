import base


class NetworkManager(base.NetworkManager):          # A class which extends the base.py's NetworkManager with a Listener and some other things
    def __init__(self):
        pass
    def initialize_listening(t_id, port):           # From this moment every packet the clients are sending to say that they are still alive will be realized and handled
        listener = Listener.__init__(t_id, base.File_Loader.get_config_string("master.conf", "Threading", "listener-name"))
        listener.start()


class Listener(threading.Thread):
    def __init__(self, threadID, name):
        base.threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self._stop_event = threading.Event()

    def stop(self):
        self._stop_event.set()
        base.running_threads.remove(self.name)

    def stopped(self):
        return self._stop_event.is_set()

    def run(self):
        pass


def check_target(target_ip, target_type, target_mac):       # This method is to check if the specified target is online or the user has permission for the type
    result = base.Database.send_query("SELECT ip, mac, type FROM " + base.get_config_string("master.conf", "Database", "table"))
    if result is not None:          # online
        if result[2] is 'cls':
            if base.get_config_string("hereconfig", "Main", "type") is 'cls':
                print("You don't have the permission to terminate a classroomserver!")      # TODO: Here we can build a nice error-message; maybe we should also do a Logger in the Base? Because normal users would not be able to even click on termintate classroom_server
                return False
        return True
    else:
        return False                # Not online


def stop_master(message):           # The message is a way to send all the clients a command why the master stops
    pass
