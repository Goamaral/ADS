class Node:
	def __init__(self,hashPais,hashSigla,pais,sigla):
		self.hashPais = hashPais
		self.hashSigla = hashSigla
		self.pais = pais
		self.sigla = sigla
		self.anos = {}
		self.next = None
		self.prev = None

	def get_data(self,ano):
		try:
			return self.anos[ano]
		except KeyError:
			return None

	def get_next(self):
		return self.next

	def set_data(self, ano, perc):
		self.anos[ano] = perc

	def set_next(self,next):
		self.next = next

	def set_prev(self,prev):
		self.prev = prev

	def get_prev(self):
		return self.prev
