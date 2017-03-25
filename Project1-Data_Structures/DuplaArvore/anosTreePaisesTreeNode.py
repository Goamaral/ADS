from hashNumber import hashNumber

class anosTreePaisesTreeNode:
	def __init__(self,pais,sigla):
		self.pais = pais
		self.hashPais = hashNumber(pais)
		self.sigla = sigla
		self.hashSigla = hashNumber(sigla)
		self.node = None

	def set_data(self,node):
		if self.node == None:
			self.node = node
			return True
		else:
			self.node.set_data(node.perc)
			return False

	def get_data(self):
		if self.node == None:
			return None
		else:
			return self.node.get_data()
