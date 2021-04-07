#!/usr/bin/env python3
"""PyBluez advanced example inquiry-with-rssi.py
Perform a simple device inquiry, followed by a remote name request of each
discovered device
"""


import sys
import os
import struct
import time
from datetime import datetime, timedelta
import bluetooth

nearby_devices = bluetooth.discover_devices(lookup_names=True)
print("Found {} devices.".format(len(nearby_devices)))

for addr, name in nearby_devices:
    print("  {} - {}".format(addr, name))