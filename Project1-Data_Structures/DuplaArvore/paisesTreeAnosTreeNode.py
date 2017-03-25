class paisesTreeAnosTreeNode:
	def __init__(self,ano):
		self.ano = ano
		self.node = None

	def set_data(self,node):
		if self.node == None:
			self.node = node
		else:
			self.node.set_data(node.perc)

	def get_data(self):
		if self.node == None:
			return None
		else:
			return self.node.get_data()
