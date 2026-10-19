from scapy.all import *

# Create an IP packet targeting 8.8.8.8 layered with an ICMP protocol header
packet = IP(dst="8.8.8.8")/ ICMP()

#send packets continuously
while (True):
    send(packet, verbose=0)
