from subprocess import call
import base
import client
import time


print = Logger.log(print)

try:
    key = base.create_random(32)
    table = base.File_Loader.get_config_string("smartdesk.conf", "Database", "table")
    mac = base.get_mac(base.File_Loader.get_config_string("smartdesk.conf", "Devices", "mac"))
    ip = base.get_ip(base.File_Loader.get_config_string("smartdesk.conf", "Devices", "ip"))

    base.Database.connect("smartdesk.conf", "Database")
    base.Database.send_query("INSERT INTO " + table + " (mac, type, ip, key)  VALUES("
                            + mac
                            + ", smd, "
                            + ip + ", "
                            + key + ")")

    client.setup_client(["smartdesk.conf", "Database", "Devices"], key, "smd")
    command_listener = client.CommandListener(0, base.File_Loader.get_config_string("smartdesk.conf", "Threading", "command_lister-name"), base.File_Loader.get_config_string("smartdesk.conf", "Networking", "command_listening-port"))
    command_listener.start()

    base.Timer(1, base.File_Loader.get_config_string("smartdesk.conf", "Threading", "refresher-name"), base.File_Loader.get_config_string("smartdesk.conf", "Threading", "refresher-time"), client.refresher())

    while True:                 # Helps security because every x seconds a new encryption key will be chosen
        time.sleep(base.File_Loader.get_config_string("smartdesk.conf", "Main", "key_gen-delay"))
        key = base.create_random(32)
        base.Database.send_query("UPDATE " + table + " SET key=" + key + " WHERE mac=" + mac + " AND ip=" + ip)
        client.setup_client(["smartdesk.conf", "Database", "Devices"], key, "smd")
except:
    print("An unexpected error occured. The system will halt NOW!")
    call["shutdown -h now"]
