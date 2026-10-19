from scapy.all import *

# Define a payload 
payload = "Hello, les amis de tekup"

# Build a packet with destination IP 192.168.1.1, TCP ports 443/443, and the payload attached
packet = IP(dst="192.168.1.1")/ TCP(sport=443, dport=443)/ payload

# Display the configured fields and layers of the packet 
packet.show()

# Re-dissect the packet after assembling and recalculating checksums and lengths
print("*********format show2************")
packet.show2()

# Print a compact one-line summary description of the packet
packet.summary()

# Transmit the packet over the network
while (True):
    send(packet, verbose=0)
