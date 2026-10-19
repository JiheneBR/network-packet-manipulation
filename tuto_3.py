from scapy.all import *

# Capture 10 live network packets
packets = sniff(count=10)

# Display detailed protocol breakdown for all captured packets
packets.show()

# Verify if the first captured packet contains an IPv4 layer
if packets[0].haslayer(IP):
    # Overwrite the packet's original source IP address with a spoofed address
    packets[0][IP].src="172.16.19.1"

# Send the first captured (and modified) packet at Layer 3
while (True):
    send(packets[0], verbose=0)


