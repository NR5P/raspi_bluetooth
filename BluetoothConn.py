from bluepy.btle import Scanner, DefaultDelegate
# https://raspberrypi.stackexchange.com/questions/114149/bluetooth-library-for-raspberry-pi 

# https://github.com/adafruit/Adafruit_CircuitPython_BLE/blob/master/examples/ble_demo_central.py

class BluetoothConn(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def handleDiscovery(self, dev, isNewDev, isNewData):
        if isNewDev:
            print("Discovered device", dev.addr)
        elif isNewData:
            print("Received new data from", dev.addr)

    def scanForDevices(self):
        scanner = Scanner().withDelegate(ScanDelegate())
        devices = scanner.scan(10.0)

        for dev in devices:
            print("Device %s (%s), RSSI=%d dB" % (dev.addr, dev.addrType, dev.rssi))
            for (adtype, desc, value) in dev.getScanData():
                print("  %s = %s" % (desc, value))
