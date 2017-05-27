from configparser import ConfigParser
import socket
import fcntl    # does only work under Linux but not under windows
import struct
import random
import sys
import mysql.connector as mc


class Database:             # Watch out here:  N O  Errors caught!
    con = None
    def __init__(self):
        pass

    def connect(database_ini_file, section):
        Database.con = mc.connect(host=File_Loader.get_config_string(database_ini_file, section, 'host'),
                                  port=File_Loader.get_config_string(database_ini_file, section, 'port'),
                                  user=File_Loader.get_config_string(database_ini_file, section, 'user'),
                                  password=File_Loader.get_config_string(database_ini_file, section, 'password'),
                                  database=File_Loader.get_config_string(database_ini_file, section, 'database'))

    def disconnect():
        Database.con.disconnect()

    def send_query(query):
        cursor = Database.con.cursor()
        cursor.execute(query)
        return cursor.fetchall()


class File_Loader:
    def __init__(self):
        pass

    def get_config_string(config_file, section, attribute):     # watch out here because of raised thingies :=)
        config = ConfigParser.read(config_file)
        config.sections()
        if not config.has_section(section):
            raise
        result = config[section][attribute]
        if result is not None:
            return result
        else:
            raise

    def set_config_string(config_file, section, attribute, value):
        config = ConfigParser.read(config_file)
        if config.has_section(section) is False:
            config.add_section(section)
        config.set(section, attribute, value)
        config.write()
        print(attribute + " from " + section + " is now " + value)


def get_ip(interface):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        ip = socket.inet_ntoa(fcntl.ioctl(s.fileno, 0x8915, struct.pack('256s', interface[:15]))[20:24])
    except:
        ip = "0.0.0.0"
    return ip

def get_mac(interface):
    try:
        mac = open('sys/class/net/' + interface + '/address').readline()
    except:
        # TODO: Beautiful error message
        mac = "00:00:00:00:00:00"
    return mac

def create_random(length):
    random.seed()
    try:
        get_char = unichr
    except:
        get_char = chr
    alphabet = [get_char(ch) for ch in range(sys.maxunicode)]
    return ''.join(random.choice(alphabet) for i in range(length))

def test_method():  # This method is only for testing the functionality of all the other methods of that module
    print(get_mac("eth0"))
    print(get_ip("eth0"))
    print(create_random(4))
    File_Loader.set_config_string('yourpath', 'Hallo', 'Test', '42')
    print(File_Loader.get_config_string('yourpath', 'Hallo', 'Test'))

test_method()       # This method is only for testing the functionality of all the other methods of that module
