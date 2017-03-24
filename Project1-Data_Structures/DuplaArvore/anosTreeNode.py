from paisesTreeAnospaisesTreeAnos import paisesTreeAnospaisesTreeAnos

class anosTreeNode:
	def __init__(self, ano):
		self.ano = ano
		self.paisesTreeAnos = paisesTreeAnospaisesTreeAnos()

#TODO - (  )
	def set_data(self,pais,sigla,node):
		self.paisesTreeAnos.insert(pais,sigla,node)
