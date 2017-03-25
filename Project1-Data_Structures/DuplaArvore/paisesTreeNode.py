from paisesTreeAnosTree import paisesTreeAnosTree

class paisesTreeNode:
	def __init__(self,pais,hashPais,sigla):
		self.pais = pais
		self.hashPais = hashPais
		self.sigla = sigla
		self.paisesTreeAnosTree = paisesTreeAnosTree()

	def set_data(self,ano,node):
		self.paisesTreeAnosTree.insert(ano,node)

	def get_data(self,ano):
		return self.paisesTreeAnosTree.get_data(ano)

	def get_list_anos(self):
		return self.paisesTreeAnosTree.collectAnos([])

	def removeAno(self, ano):
		self.paisesTreeAnosTree.remove(ano)
