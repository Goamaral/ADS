from dicSiglasNode import dicSiglasNode

class dicSiglas:
	def __init__(self):
		self.node = None
		self.height = -1
		self.balance = 0

	def add(self,sigla,pais):
		newnode = dicSiglasNode(sigla,pais)
		hashSigla = hash(sigla)

		if self.node == None:
			self.node = newnode
			self.node.left = dicSiglas()
			self.node.right = dicSiglas()
		else:
			if hashSigla < self.node.hashSigla:
				self.node.left.add(sigla,pais)
			elif hashSigla > self.node.hashSigla:
				self.node.right.add(sigla,pais)
			else:
				return

		self.rebalance()

	def search(self, input):
		hashSigla = hash(input)
		if self.node == None:
			return None
		if hashSigla > self.node.hashSigla:
			return self.node.right.search(hashSigla)
		elif hashSigla < self.node.hashSigla:
			return self.node.left.search(hashSigla)
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
