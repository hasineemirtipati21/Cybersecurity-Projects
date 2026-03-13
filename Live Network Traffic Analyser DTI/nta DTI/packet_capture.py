from scapy.all import sniff, IP
import csv

def process_packet(packet):
    if packet.haslayer(IP):

        src = packet[IP].src
        dst = packet[IP].dst
        proto = packet[IP].proto
        size = len(packet)

        if proto == 6:
            proto_name = "TCP"
        elif proto == 17:
            proto_name = "UDP"
        elif proto == 1:
            proto_name = "ICMP"
        else:
            proto_name = "OTHER"

        with open("traffic_data.csv","a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([src, dst, proto_name, size])

print("Capturing packets...")
sniff(prn=process_packet, store=False)