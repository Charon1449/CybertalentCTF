from scapy.all import *
import base64

packets = rdpcap('ARP+Storm.pcap')


message = ''
for packet in packets:
    message += chr(packet.op)

print(base64.b64decode(message))
