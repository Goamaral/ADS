from ListNode import ListNode
from hashNumber import hashNumber

debugging = True

def debug(msg):
	if debugging:
		print msg

#Mode 0: nome
#Mode 1: sigla

class List:
	def __init__(self):
		self.head = None

	def removeAno(self, ano):
		if self.head == None:
			return None

		current = self.head

		while current.next != self.head:
			current.removeAno(ano)
			current = current.next

		current.removeAno(ano)

	def collectPaisesAno(self, ano, l):
		if self.head == None:
			return l

		current = self.head

		while current.next != self.head:
			perc = current.get_data(ano)
			if perc != None:
				obj = {}
				obj[current.pais] = perc
				l.append(obj)
			current = current.next

		perc = current.get_data(ano)
		if perc != None:
			obj = {}
			obj[current.pais] = perc
			l.append(obj)

		return l

	def insert(self,pais,sigla,ano,perc):
		hashPais = hashNumber(pais)
		hashSigla = hashNumber(sigla)

		current = self.head
		#vazio
		if self.head == None:
			newNode = ListNode(hashPais,hashSigla,pais,sigla);
			self.head = newNode;
			newNode.next = self.head
			newNode.prev = self.head
			newNode.set_data(ano,perc)
			return (True, newNode, 'vazio')
		#um no
		elif self.head.next == self.head:
			#pais existente
			if self.head.hashPais == hashPais:
				self.head.set_data(ano,perc)
				return (False, None, None)
			#pais nao existente
			else:
				#antes da cabeca
				if hashPais < self.head.hashPais:
					newNode = ListNode(hashPais,hashSigla,pais,sigla)
					prevNode = self.head.prev
					newNode.next = self.head
					self.head.prev = newNode
					newNode.prev = prevNode
					prevNode.next = newNode
					self.head = newNode
					return (True, newNode, 'um')
				elif hashPais > self.head.hashPais:
					newNode = ListNode(hashPais,hashSigla,pais,sigla)
					self.head.next = newNode
					self.head.prev = newNode
					newNode.next = self.head
					newNode.prev = self.head
					newNode.set_data(ano,perc)
					return (True, newNode, 'um')
				else:
					raise ValueError('Erro a inserir quando so ha um no')
		#multiplos nos
 		else:
			#pais encontrado na cabeca
			if current.hashPais == hashPais:
				current.set_data(ano,perc)
				return (False, None, None)
			#pais nao encontrado na cabeca
			else:
				#antes da cabeca
				if hashPais < current.hashPais:
					prevNode = current.prev
					newNode = ListNode(hashPais,hashSigla,pais,sigla)
					newNode.set_data(ano,perc)
					prevNode.next = newNode
					newNode.prev = prevNode
					current.prev = newNode
					newNode.next = current
					self.head = newNode
					return (True, newNode, 'antes da cabeca')
				elif hashPais > current.hashPais:
					current = current.next

			while current.next != self.head:
				#pais encontrado
				if current.hashPais == hashPais:
					current.set_data(ano,perc)
					return (False, None, None)
				#pais nao encontrado ainda
				else:
					#antes do no atual
					if hashPais < current.hashPais:
						prevNode = current.prev
						newNode = ListNode(hashPais,hashSigla,pais,sigla)
						newNode.set_data(ano,perc)
						prevNode.next = newNode
						newNode.prev = prevNode
						current.prev = newNode
						newNode.next = current
						return (True, newNode, 'antes do atual')
					elif hashPais > current.hashPais:
						current = current.next

			if current.next == self.head:
				if current.hashPais == hashPais:
					current.set_data(ano,perc)
					return (False, None, None)
				else:
					if hashPais < current.hashPais:
						prevNode = current.prev
						newNode = ListNode(hashPais,hashSigla,pais,sigla)
						newNode.set_data(ano,perc)
						prevNode.next = newNode
						newNode.prev = prevNode
						current.prev = newNode
						newNode.next = current
						return (True, newNode, 'penultimo')
					elif hashPais > current.hashPais:
						newNode = ListNode(hashPais,hashSigla,pais,sigla)
						newNode.set_data(ano,perc)
						newNode.next = self.head
						self.head.prev = newNode
						newNode.prev = current
						current.next = newNode
						return (True, newNode, 'ultimo')

	def removeNode(self,node):
		prevNode = node.prev
		nextNode = node.next
		node.prev = None
		node.next = None

		#so um no
		if node == self.head and nextNode == self.head:
			self.head = None
		else:
			#meio da lista ou fim com mais que um no
			prevNode.next = nextNode
			nextNode.prev = prevNode
			#inicio com mais que um no
			if node == self.head:
				self.head = nextNode


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

	def rightSearch(self, mode, hashCode):
		current = self.head
		if self.head == None:
			return None
		if mode == 0:
			if hashCode == current.hashPais:
				return current
			else:
				while current.next != self.head:
					if hashCode == current.hashPais:
						return current
					current = current.next
				if hashCode == current.hashPais:
					return current
				return None
		else:
			if hashCode == current.hashSigla:
				return current
			else:
				while current.next != self.head:
					if current.hashSigla == hashCode:
						return current
					current = current.next
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
				while current.prev != self.head:
					if hashCode == current.hashPais:
						return current
					current = current.prev
				if hashCode == current.hashPais:
					return current
				return None
		else:
			if current.hashSigla == hashCode:
				return current
			else:
				while current.prev != self.head:
					if current.hashSigla == hashCode:
						return current
					current = current.prev
				if current.hashSigla == hashCode:
					return current
				return None
