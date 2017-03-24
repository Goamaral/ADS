class Node:
	def __init__(self, perc):
		self.perc = perc
		self.paisNode = None
		self.anoNode = None

	def setPaisLink(self, paisNode):
		self.paisNode = paisNode

	def setAnoLink(self, anoNode):
		self.anoNode = anoNode

	def clearNode(self):
		self.perc = None
		self.paisNode = None
		self.anoNode = None
