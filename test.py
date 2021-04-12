# SPDX-FileCopyrightText: 2020 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""
This example scans for any BLE advertisements and prints one advertisement and one scan response
from every device found.
"""

from adafruit_ble import BLERadio
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.nordic import UARTService

ble = BLERadio()
device_addr = "f4:cf:a2:8d:30:fa"
print("scanning")
found = set()
scan_responses = set()
uart_connection = None
for advertisement in ble.start_scan():
    if device_addr.lower() in str(advertisement.address):
        addr = advertisement.address
        print(addr)
        #print(advertisement.services) 
        uart_connection = ble.connect(advertisement) 
        if advertisement.scan_response and addr not in scan_responses:
            scan_responses.add(addr)
        elif not advertisement.scan_response and addr not in found:
            found.add(addr)
        else:
            continue
        print(addr, advertisement)
        print("\t" + repr(advertisement))
        print()

print("scan done")

print(ble.connected)
while ble.connected:
    one_byte = ble.read(1)
    print(one_byte)

