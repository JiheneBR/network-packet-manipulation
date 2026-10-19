from scapy.all import *

# Create an IP packet aimed at 192.168.1.1 stacked with a TCP header (source port 443, destination port 80)
packet = IP(dst="192.168.1.1")/ TCP(sport=443, dport=80)

# Send the packet at the network layer
while (True):
    send(packet, verbose=0)