class dicSiglasNode:
	def __init__(self,sigla,pais):
		self.hashSigla = hash(sigla)
		self.pais = pais
