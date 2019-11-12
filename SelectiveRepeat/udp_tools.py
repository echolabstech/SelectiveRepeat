from PyCRC.CRC16 import CRC16
from collections import namedtuple

PACKET = namedtuple("Packet", ["SequenceNumber", "Checksum", "Data"])
ACK = namedtuple("ACK", ["AckNumber", "Checksum"])

class PacketTools(object):
	@staticmethod
	def checksum(data):
		return CRC16().calculate(data)

	@staticmethod
	def update_Ack(original_ack, ack_number=None, check_sum=None):
		ack_number = ack_number if ack_number != None else original_ack.AckNumber
		check_sum = check_sum if check_sum != None else original_ack.Checksum
		return ACK(AckNumber=ack_number, Checksum=check_sum)
