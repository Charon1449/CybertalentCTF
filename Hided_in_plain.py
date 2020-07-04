from scapy.all import *
import base64
from yenc import decode


def get_ICMP_data(filename):
    capture = rdpcap(filename)
    ping_data = ""
    for packet in capture:
        if packet[ICMP].type == 8: # Echo request
             ping_data += str(packet[Raw])
    return ping_data

encrypted_data = ""
encrypted_data += get_ICMP_data("f101.pcap")
open('encrypted_data' ,"w").write(encrypted_data)
decode('encrypted_data','decrypted.txt')
