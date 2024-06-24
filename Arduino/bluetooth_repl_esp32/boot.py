from machine import Pin
import ubluetooth
import webrepl
import network
import time
import ed

from ed import mydir, printf, printsrc, printdef, onlydefs
from ed import write, append, edit, apply, editdef, ls
from ed import writef, insertf, appendf, undo

time.sleep(2.0)
print("Running boot.py - network station, webrepl.")

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect("DIGI-77CA", "QqiD8937")
webrepl.start()


def ifconfig():
    print("network active: ", sta_if.isconnected())
    print("network config: ", sta_if.ifconfig())


def p(*argv):
    ble.send(" ".join(str(arg) for arg in argv))
    time.sleep(0.125)


def pstr(*argv):
    ble.send(" ".join(
        (str(arg) if str != type(arg) else '"' + arg + '"') for arg in argv))
    time.sleep(0.125)


ed.p = p
ed.pstr = pstr


class BLE():
    def __init__(self, name):
        self.name = name
        self.ble = ubluetooth.BLE()
        self.ble.active(True)

        self.led = Pin(2, Pin.OUT)

        self.ble = ubluetooth.BLE()
        self.ble.active(True)
        self.disconnected()
        self.ble.irq(self.ble_irq)
        self.register()
        self.advertiser()

    def connected(self):
        pass

    def disconnected(self):
        pass

    def ble_irq(self, event, data):
        if event == 1:
            self.connected()
        elif event == 2:
            self.advertiser()
            self.disconnected()
        elif event == 3:
            buf = self.ble.gatts_read(self.rx)
            buf = buf.decode('UTF-8').rstrip()
            ed.command(buf, globals())

    def register(self):
        NUS_UUID = '6E400001-B5A3-F393-E0A9-E50E24DCCA9E'
        RX_UUID = '6E400002-B5A3-F393-E0A9-E50E24DCCA9E'
        TX_UUID = '6E400003-B5A3-F393-E0A9-E50E24DCCA9E'
        BLE_NUS = ubluetooth.UUID(NUS_UUID)
        BLE_RX = (ubluetooth.UUID(RX_UUID), ubluetooth.FLAG_WRITE)
        BLE_TX = (ubluetooth.UUID(TX_UUID), ubluetooth.FLAG_NOTIFY)
        BLE_UART = (BLE_NUS, (BLE_TX, BLE_RX))
        SERVICES = (BLE_UART, )
        self.tx, self.rx, = self.ble.gatts_register_services(SERVICES)[0]
        self.ble.gatts_write(self.rx, bytes(160))

    def send(self, data):
        self.ble.gatts_notify(0, self.tx, data + '\n')

    def advertiser(self):
        name = bytes(self.name, 'UTF-8')
        adv_data = bytearray('\x02\x01\x02') + bytearray(
            (len(name) + 1, 0x09)) + name
        self.ble.gap_advertise(100, adv_data)


ble = BLE('ESP32BLE1')
