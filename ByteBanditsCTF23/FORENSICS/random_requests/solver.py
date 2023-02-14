#!/usr/bin/env python3
from scapy.all import *
from base64 import *

packets = rdpcap("random_requests.pcapng")

binary_output = ""

for packet in packets:
    if packet[IP].dst == "142.250.67.132" and packet.haslayer(Raw):
        binary_output += packet[Raw].load.split(b" ")[1].decode().split("=")[1]

output = binary_output.replace("%20", " ")

with open("output.txt", "w") as file:
    file.write(output)