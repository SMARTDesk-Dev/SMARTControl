import socket
import fcntl
import struct
import random
import sys

class File_Loader:
    def __init__(self):
        pass
    def get_string():
        return None

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
