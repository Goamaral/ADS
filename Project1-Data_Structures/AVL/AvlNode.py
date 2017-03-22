from anosAvl import anosAvl

class AvlNode():
	def __init__(self,hashPais,pais,sigla):
		self.hashPais = hashPais
		self.pais = pais
		self.sigla = sigla
		self.anos = anosAvl()
		self.left = None
		self.right = None

	def set_data(self, ano, perc):
		return self.anos.add(ano, perc)

	def get_data(self,ano):
		return self.anos.get_data(ano)

	def get_list_anos(self):
		return self.anos.get_list_anos([])

	def removeAno(self, ano):
		self.anos.remove(ano)
