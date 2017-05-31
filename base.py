# This module will be a pool of useful methods and classes
from configparser import ConfigParser
import socket
import fcntl    # does only work under Linux but not under windows
import struct
import random
import sys
import mysql.connector as mc    # you will need to install mysql for this import


running_threads[]

class Crypter:              # This class will encrypt and decrypt a text for network traffic
    def __init__(self):
        pass

    def encrypt(password, key, text):
        pass

    def decrypt(password, key, text):
        pass


class Database:             # Watch out here:  N O  Errors caught! In this class every Database related aspect is done
    _con = None             # Don't use this variable but the methods which are also in this class
    def __init__(self):
        pass

    def connect(database_ini_file, section):
        Database._con = mc.connect(host=File_Loader.get_config_string(database_ini_file, section, 'host'),
                                  port=File_Loader.get_config_string(database_ini_file, section, 'port'),
                                  user=File_Loader.get_config_string(database_ini_file, section, 'user'),
                                  password=File_Loader.get_config_string(database_ini_file, section, 'password'),
                                  database=File_Loader.get_config_string(database_ini_file, section, 'database'))

    def disconnect():
        Database._con.disconnect()

    def send_query(query):      # This method will be the method to send SQL commands and will also return all given results
        cursor = Database._con.cursor()
        cursor.execute(query)
        return cursor.fetchall()


class NetworkManager:           # This class will secure the communication with other Devices in the Network
    def __init__(self):
        pass

    def send_packet(target_ip, target_port, packet):
        s = socket.socket()
        s.connect((target_ip, target_port))
        if packet.length > 1024:
            raise
        s.send(packet)
        s.close()

    def listen(port):           # I maybe have to open a new thread which gets all commands in offline time. But that needs some testing time
        s = socket.socket()
        host = socket.gethostname()
        s.bind((host, port))

        s.listen(10000000)
        result = s.recv(1024)
        s.close()
        return result


class Timer(threading.Thread):
    def __init__(self, threadID, name, time, method_to_execute):        # time = waiting_time
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.time = time
        self.execute = method_to_execute

    def run(self):
        running_threads.append(self.name)
        while True:
            time.sleep(self.time)                                       # The waiting_time applies here
            self.execute()                                              # Execute method which is selected in the constructor


class File_Loader:              # To make life easier with files use the methods in this class (up to this moment there is only the ConfigParser-Reader and -Writer because no other type is needed)
    def __init__(self):
        pass

    def get_config_string(config_file, section, attribute):     # Watch out here because of raised thingies :=). Gives back a string or raises
        config = ConfigParser.read(config_file)
        config.sections()
        if not config.has_section(section):
            raise
        result = config[section][attribute]
        if result is not None:
            return result
        else:
            raise

    def set_config_string(config_file, section, attribute, value):      # Watch out here because no errors are caught
        config = ConfigParser.read(config_file)
        if config.has_section(section) is False:
            config.add_section(section)
        config.set(section, attribute, value)
        config.write()
        print(attribute + " from " + section + " is now " + value)


def get_ip(interface):      # Gives back the ip-address for the given interface
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        ip = socket.inet_ntoa(fcntl.ioctl(s.fileno, 0x8915, struct.pack('256s', interface[:15]))[20:24])
    except:
        ip = "0.0.0.0"
    return ip

def get_mac(interface):     # Gives back the mac-address for the given interface or if the interface is not availeble 00:00:00:00:00:00
    try:
        mac = open('sys/class/net/' + interface + '/address').readline()
    except:
        # TODO: Beautiful error message
        mac = "00:00:00:00:00:00"
    return mac

def create_random(length):  # This method gives back a random string for the key and the password which will be generated every time when the module starts
    random.seed()
    try:
        get_char = unichr
    except:
        get_char = chr
    alphabet = [get_char(ch) for ch in range(sys.maxunicode)]
    return ''.join(random.choice(alphabet) for i in range(length))

def test_method():          # This method is only for testing the functionality of all the other methods of that module
    print(get_mac("eth0"))
    print(get_ip("eth0"))
    print(create_random(4))
    File_Loader.set_config_string('yourpath', 'Hello', 'Test', '42')
    print(File_Loader.get_config_string('yourpath', 'Hello', 'Test'))
    try:
        Database.connect("hereinifile", "heresection")
        Database.send_query("SELECT* FROM tablehere")
        Database.disconnect()
    except:
        print("something went wrong")


test_method()               # This method is only for testing the functionality of all the other methods of that module
