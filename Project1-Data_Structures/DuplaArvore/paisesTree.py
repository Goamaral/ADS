from paisesTreeNode import paisesTreeNode
from hashNumber import hashNumber

class paisesTree:
	def __init__(self):
		self.node = None
		self.height = -1
		self.balance = 0;

	def removeAno(self, ano):
		if self.node == None:
			return None

		left = self.node.left != None
		right = self.node.right != None

		self.node.removeAno(ano)

		if left and right:
			self.node.left.removeAno(ano)
			self.node.right.removeAno(ano)
			return None
		elif left:
			self.node.left.removeAno(ano)
			return None
		elif right:
			self.node.right.removeAno(ano)
			return None
		else:
			return None

	def insert(self,pais,sigla,ano,node):
		hashPais = hashNumber(pais)

		if self.node == None:
			newnode = paisesTreeNode(pais,hashPais,sigla)
			newnode.set_data(ano,node)
			self.node = newnode
			self.node.left = paisesTree()
			self.node.right = paisesTree()
			self.rebalance()
			return
		else:
			if hashPais < self.node.hashPais:
				self.node.left.insert(pais,sigla,ano,node)
			elif hashPais > self.node.hashPais:
				self.node.right.insert(pais,sigla,ano,node)
			elif hashPais == self.node.hashPais:
				self.node.set_data(ano,node)
				return
			self.rebalance()

	def listPaises(self):
		if self.node == None:
			return
		print self.node.pais
		if self.node.right != None and self.node.left != None:
			self.node.left.listPaises()
			self.node.right.listPaises()
		elif self.node.right != None:
			self.node.right.listPaises()
		elif self.node.left != None:
			self.node.left.listPaises()
		else:
			self.node

	def searchByPais(self, hashPais):
		if self.node == None:
			return None
		if hashPais > self.node.hashPais:
			return self.node.right.searchByPais(hashPais)
		elif hashPais < self.node.hashPais:
			return self.node.left.searchByPais(hashPais)
		else:
			return self.node

	def remove(self, input):
		hashPais = hashNumber(input)
		if self.node != None:
			if self.node.hashPais == hashPais:
				if self.node.left.node == None and self.node.right.node == None:
					self.node = None
				elif self.node.left.node == None:
					self.node = self.node.right.node
				elif self.node.right.node == None:
					self.node = self.node.left.node
				else:
					replacement = self.logical_successor(self.node)
					if replacement != None:
						self.node.pais = replacement.pais
						self.node.hashPais = replacement.hashPais
						self.node.sigla = replacement.sigla
						self.node.paisesTreeAnosTree = replacement.paisesTreeAnosTree
						self.node.right.remove(replacement.pais)

				self.rebalance()
				return True
			elif hashPais < self.node.hashPais:
				return self.node.left.remove(input)
			elif hashPais > self.node.hashPais:
				return self.node.right.remove(input)

			self.rebalance()

		return False

	### BALANCE AND ROTATIONS
	def rebalance(self):
		self.update_heights(False)
		self.update_balances(False)
		while self.balance < -1 or self.balance > 1:
			if self.balance > 1:
				if self.node.left.balance < 0:
					self.node.left.lrotate() # we're in case II
					self.update_heights()
					self.update_balances()
				self.rrotate()
				self.update_heights()
				self.update_balances()

			if self.balance < -1:
				if self.node.right.balance > 0:
					self.node.right.rrotate() # we're in case III
					self.update_heights()
					self.update_balances()
				self.lrotate()
				self.update_heights()
				self.update_balances()

	def rrotate(self):
		A = self.node
		B = self.node.left.node
		T = B.right.node

		self.node = B
		B.right.node = A
		A.left.node = T

	def lrotate(self):
		A = self.node
		B = self.node.right.node
		T = B.left.node

		self.node = B
		B.left.node = A
		A.right.node = T

	def update_heights(self, recurse=True):
		if not self.node == None:
			if recurse:
				if self.node.left != None:
					self.node.left.update_heights()
				if self.node.right != None:
					self.node.right.update_heights()

			self.height = max(self.node.left.height,self.node.right.height) + 1
		else:
			self.height = -1

	def update_balances(self, recurse=True):
		if not self.node == None:
			if recurse:
				if self.node.left != None:
					self.node.left.update_balances()
				if self.node.right != None:
					self.node.right.update_balances()

			self.balance = self.node.left.height - self.node.right.height
		else:
			self.balance = 0
