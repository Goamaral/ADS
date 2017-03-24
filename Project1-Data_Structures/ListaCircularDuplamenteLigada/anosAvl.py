from anosNode import anosNode
from hashNumber import hashNumber

class anosAvl:
	def __init__(self):
		self.node = None
		self.height = -1
		self.balance = 0

	def get_list_anos(self, l):
		if self.node == None:
			return l

		left = self.node.left != None
		right = self.node.right != None

		perc = self.node.get_data()
		if perc != None:
			obj = {}
			obj[self.node.ano] = perc
			l.append(obj)

		if left and right:
			l = self.node.left.get_list_anos(l)
			l = self.node.right.get_list_anos(l)
			return l
		elif left:
			return self.node.left.get_list_anos(l)
		elif right:
			return self.node.right.get_list_anos(l)
		else:
			return l

	def set_data(self, ano, perc):
		result = self.searchNode(ano)
		if result != None:
			result.set_data(perc)
		else:
			self.add(ano,perc)

	def get_data(self, ano):
		result = self.searchNode(ano)
		if result != None:
			return result.get_data()
		else:
			return None

	def searchNode(self, ano):
		if self.node == None:
			return None
		if ano > self.node.ano:
			return self.node.right.searchNode(ano)
		elif ano < self.node.ano:
			return self.node.left.searchNode(ano)
		else:
			return self.node

	def add(self,ano,perc):
		newnode = anosNode(ano,perc)

		if self.node == None:
			self.node = newnode
			self.node.left = anosAvl()
			self.node.right = anosAvl()
		else:
			if ano < self.node.ano:
				self.node.left.add(ano,perc)
			elif ano > self.node.ano:
				self.node.right.add(ano,perc)
			else:
				self.node.perc = perc

		self.rebalance()

	def search(self, input):
		hashSigla = hashNumber(input)
		if self.node == None:
			return None
		if hashSigla > self.node.hashSigla:
			return self.node.right.search(input)
		elif hashSigla < self.node.hashSigla:
			return self.node.left.search(input)
		else:
			return self.node.pais

	### HEIGHT AND IS_LEAF
	def height(self):
		if self.node:
			return self.node.height
		else:
			return 0

	def is_leaf(self):
		return (self.height == 0)

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

	def logical_successor(self, node):
		node = node.right.node
		if node != None:
			while node.left != None:
				if node.left.node == None:
					return node
				else:
					node = node.left.node
		return node

	def remove(self, ano):
		if self.node != None:
			if self.node.ano == ano:
				if self.node.left.node == None and self.node.right.node == None:
					self.node = None
				elif self.node.left.node == None:
					self.node = self.node.right.node
				elif self.node.right.node == None:
					self.node = self.node.left.node
				else:
					replacement = self.logical_successor(self.node)
					if replacement != None:
						self.node.ano = replacement.ano
						self.node.perc = replacement.perc
						self.node.right.remove(replacement.ano)

				self.rebalance()
				return
			elif ano < self.node.ano:
				self.node.left.remove(ano)
			elif ano > self.node.ano:
				self.node.right.remove(ano)

			self.rebalance()
		else:
			return
