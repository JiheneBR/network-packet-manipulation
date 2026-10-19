from scapy.all import *

# Capture 10 incoming or outgoing network packets from the active interface
packets = sniff(count=10)

# Display a summary of all captured packets
packets.nsummary()

# Print a detailed multi-layer breakdown of the 6th captured packet (index 5)
packets[5].show()