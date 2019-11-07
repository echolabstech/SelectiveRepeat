from PyCRC.CRC16 import CRC16

class PacketTools(object):
    def checksum(self, data):
        """
        Compute and return a checksum of the given payload data.
        """
        # Force payload data into 16 bit chunks
        try:
            if (len(data) % 2) != 0:
                data += "0"

            sum = 0
            for i in range(0, len(data), 2):
                data16 = ord(data[i]) + (ord(data[i+1]) << 8)
                sum = self.carry_around_add(sum, data16)

            return ~sum & 0xffff
        except Exception as e:
            return CRC16().calculate(data)

    def carry_around_add(self, sum, data16):
        """
        Helper function for carry around add.
        """
        sum = sum + data16
        return (sum & 0xffff) + (sum >> 16)
