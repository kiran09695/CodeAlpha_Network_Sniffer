from scapy.all import sniff

def packet_handler(packet):
    print(packet.summary())

print("Network Sniffer Started...")

sniff(prn=packet_handler, count=10)
