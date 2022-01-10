#used to parsing arguments
import argparse
#used to extract information from pcap files
from scapy.all import *
#used for operations involving IP addresses
import ipaddress

#parse arguments
parser = argparse.ArgumentParser(description="Extract Useful Information From .pcap")
parser.add_argument("pcap_name")
args = parser.parse_args()
pcap_file_name = args.pcap_name
#extracts a list of IP address, removing local IP addresses in the process
def extract_IP():
    source_ip = []
    dest_ip = []
    #open PCAP
    packets = rdpcap(pcap_file_name)
    for packet in packets:
        source_ip.append(packet[IP].src)
        dest_ip.append(packet[IP].dst)
    print(set(dest_ip))
    print(set(source_ip))

if __name__ == '__main__':
    extract_IP()