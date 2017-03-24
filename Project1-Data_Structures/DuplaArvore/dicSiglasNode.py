from hashNumber import hashNumber

class dicSiglasNode:
	def __init__(self,sigla,pais):
		self.hashSigla = hashNumber(sigla)
		self.pais = pais
