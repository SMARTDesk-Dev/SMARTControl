import base

def check_target(target_ip, target_type, target_mac):       # This method is to check if the specified target is online or the user has permission for the type
    result = base.Database.send_query("SELECT ip, mac, type FROM " + base.get_config_string("herethefile", "Database", "online_table"))
    if result is not None:          # online
        if result[2] is 'classroom_server':
            if base.get_config_string("hereconfig", "Main", "type") is 'classroom_server':
                print("You don't have the permission to terminate a classroomserver!")      # TODO: Here we can build a nice error-message; maybe we should also do a Logger in the Base? Because normal users would not be able to even click on termintate classroom_server
                return False
        return True
    else:
        return False                # Not online


class NetworkManager(base.NetworkManager):          # A class which extends the base.py's NetworkManager with a Listener and some other things
    def __init__(self):
        pass
