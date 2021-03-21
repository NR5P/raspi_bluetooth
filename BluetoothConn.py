# https://raspberrypi.stackexchange.com/questions/114149/bluetooth-library-for-raspberry-pi 

# https://github.com/adafruit/Adafruit_CircuitPython_BLE/blob/master/examples/ble_demo_central.py

from adafruit_ble import BLERadio
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.nordic import UARTService
import time

class BluetoothConn():
    def __init__(self):
        self._ble = BLERadio()
        self.conn = None

    def start(self):
        while True:
            self.scanForDevices()

    def scanForDevices(self):
        if not self.conn:
            print("scanning....")
            for bconn in self._ble.start_scan(ProvideServicesAdvertisement, timeout=5):
                print(bconn)
                if UARTService in bconn.services:
                    print("found a UARTService advertisement")
                    self.conn = self._ble.connect(adv)
                    break
            self._ble.stop_scan()
        while self.conn and self.conn.connected:
            time.sleep(1)
            print("connected still")

        # Stop scanning whether or not we are connected.
        self._ble.stop_scan()
