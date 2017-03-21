from Node import Node

debugging = True

def debug(msg):
	if debugging:
		print msg

#Mode 0: nome
#Mode 1: sigla

class ListaCirculasDuplamenteLigada:
	def __init__(self):
		self.head = None

	def insert(self,pais,sigla,ano,perc):
		hashPais = hash(pais)
		hashSigla = hash(sigla)

		current = self.head
		if self.head == None:
			newNode = Node(hashPais,hashSigla,pais,sigla);
			self.head = newNode;
			newNode.set_next(self.head)
			newNode.set_prev(self.head)
			newNode.set_data(ano,perc)
		elif self.head != None and self.head.get_next() == self.head:
			if self.head.hashPais == hashPais:
				self.head.set_data(ano,perc)
			else:
				newNode = Node(hashPais,hashSigla,pais,sigla)
				self.head.set_next(newNode)
				self.head.set_prev(newNode)
				newNode.set_next(self.head)
				newNode.set_prev(self.head)
				newNode.set_data(ano,perc)
 		else:
			while current.get_next() != self.head:
				if current.sigla == sigla:
					current.set_data(ano,perc)
					break
				else:
					current = current.get_next()
			if current.get_next() == self.head:
				if current.hashPais == hashPais:
					current.set_data(ano,perc)
				else:
					newNode = Node(hashPais,hashSigla,pais,sigla)
					newNode.set_next(self.head)
					newNode.set_prev(current)
					current.set_next(newNode)
					self.head.set_prev(newNode)
					newNode.set_data(ano,perc)

	def remove(self,mode,nome,ano):
		result = self.searchNode(mode, nome)
		if result != None:
			result.set_data(ano,None)
		else:
			debug('Pais nao encontrado')

	def edit(self,mode,nome,ano,perc):
		result = self.searchNode(mode, nome)
		if result == None:
			debug('Pais nao encontrado')
			return None
		else:
			return result.set_data(ano,perc)

	def search(self, mode, nome, ano):
		result = self.searchNode(mode, nome)
		if result == None:
			debug('Pais nao encontrado')
			return None
		else:
			return result.get_data(ano)

	def searchNode(self, mode, nome):
		current = self.head
		if mode == 0:
			ncurrent = ord(current.pais[0])
			nprev = ord(current.get_prev().pais[0])
			npesquisa = ord(nome[0])
		else:
			ncurrent = ord(current.sigla[0])
			nprev = ord(current.get_prev().sigla[0])
			npesquisa = ord(nome[0])

		media = (ncurrent + nprev)/2

		hashCode = hash(nome)

		if npesquisa > media:
			return self.leftSearch(mode, hashCode)
		else:
			return self.rightSearch(mode, hashCode)

	def rightSearch(self, mode, hashCode):
		current = self.head
		if self.head == None:
			return None
		if mode == 0:
			if hashCode == self.node.hashPais:
				return current
			else:
				while current.get_next() != self.head:
					if hashCode == current.hashPais:
						return current
					current = current.get_next()
				if hashCode == current.hashPais:
					return current
				return None
		else:
			if hashCode == self.node.hashSigla:
				return current
			else:
				while current.get_next() != self.head:
					if current.hashSigla == hashCode:
						return current
					current = current.get_next()
				if current.hashSigla == hashCode:
					return current
				return None

	def leftSearch(self, mode, hashCode):
		if self.head == None:
			return None
		current = self.head
		if mode == 0:
			if hashCode == current.hashPais:
				return current
			else:
				while current.get_prev() != self.head:
					if hashCode == current.hashPais:
						return current
					current = current.get_prev()
				if hashCode == current.hashPais:
					return current
				return None
		else:
			if current.hashSigla == hashCode:
				return current
			else:
				while current.get_prev() != self.head:
					if current.hashSigla == hashCode:
						return current
					current = current.get_prev()
				if current.hashSigla == hashCode:
					return current
				return None
