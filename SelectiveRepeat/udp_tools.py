from PyCRC.CRC16 import CRC16

class PacketTools(object):
    def checksum(self, data):
        return CRC16().calculate(data)
