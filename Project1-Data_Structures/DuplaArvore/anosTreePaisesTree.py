from anosTreePaisesTreeNode import anosTreePaisesTreeNode
from hashNumber import hashNumber

class anosTreePaisesTree:
	def __init__(self):
		self.node = None
		self.height = -1
		self.balance = 0;

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
						self.node.hashSigla = replacement.hashSigla
						self.node.node = replacement.node
						self.node.right.remove(replacement.pais)

				self.rebalance()
				return True
			elif input < self.node.hashPais:
				return self.node.left.remove(input)
			elif input > self.node.hashPais:
				return self.node.right.remove(input)

			self.rebalance()

		return False

	def insert(self,pais,sigla,node):
		notDone = None
		if self.node == None:
			self.node = anosTreePaisesTreeNode(pais,sigla)
			notDone = self.node.set_data(node)
			self.node.left = anosTreePaisesTree()
			self.node.right = anosTreePaisesTree()
		else:
			notDone = 0
			hashPais = hashNumber(pais)
			if hashPais < self.node.hashPais:
				notDone = self.node.left.insert(pais,sigla,node)
			elif hashPais > self.node.hashPais:
				notDone = self.node.right.insert(pais,sigla,node)
			elif hashPais == self.node.hashPais:
				notDone = self.node.set_data(node)

		self.rebalance()
		if notDone != None and notDone != 0:
			return notDone

	def collectPaises(self,l):
		if self.node == None:
			return l

		left = self.node.left != None
		right = self.node.right != None

		perc = self.node.get_data();
		if perc != None:
			obj = {}
			obj[self.node.pais] = perc
			l.append(obj)

		if left and right:
			l = self.node.left.collectPaises(l)
			l = self.node.right.collectPaises(l)
			return l
		elif left:
			return self.node.left.collectPaises(l)
		elif right:
			return self.node.right.collectPaises(l)
		else:
			return l

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
