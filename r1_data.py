#!/usr/bin/env python

import re

r1_dict = {}

f = open("r1_cdp.txt")

for line in f:
    device = re.search(r"Device ID: (.+)", line)
    if device:
        r1_dict['Device Name'] = device.group(1)

    ip_addr = re.search(r"IP address: (.+)", line)
    if ip_addr:
        r1_dict['IP'] = ip_addr.group(1)

    vendor = re.search(r"Platform: (.+?) (.+?),  Capabilities: (.+)", line)
    if vendor:
        r1_dict['Vendor'] = vendor.group(1)
        r1_dict['Model'] = vendor.group(2)
        r1_dict['Device Type'] = vendor.group(3)

#print r1_dict

print
output_control = ('Device Name', 'IP', 'Vendor', 'Model', 'Device Type')
for element in output_control:
    print "%20s: % -20s" % (element, r1_dict[element])

print

