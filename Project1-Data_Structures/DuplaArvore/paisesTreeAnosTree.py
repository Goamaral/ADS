from paisesTreeAnosTreeNode import paisesTreeAnosTreeNode

class paisesTreeAnosTree:
	def __init__(self):
		self.node = None
		self.height = -1
		self.balance = 0;

	def collectAnos(self,l):
		if self.node == None:
			return l

		left = self.node.left != None
		right = self.node.right != None

		perc = self.node.get_data();
		if perc != None:
			obj = {}
			obj[self.node.ano] = perc
			l.append(obj)

		if left and right:
			l = self.node.left.collectAnos(l)
			l = self.node.right.collectAnos(l)
			return l
		elif left:
			return self.node.left.collectAnos(l)
		elif right:
			return self.node.right.collectAnos(l)
		else:
			return l

	def insert(self,ano,node):
		if self.node == None:
			newnode = paisesTreeAnosTreeNode(ano)
			newnode.set_data(node)
			self.node = newnode
			self.node.left = paisesTreeAnosTree()
			self.node.right = paisesTreeAnosTree()
			self.rebalance()
			return
		else:
			if ano < self.node.ano:
				self.node.left.insert(ano,node)
			elif ano > self.node.ano:
				self.node.right.insert(ano,node)
			elif ano == self.node.ano:
				self.node.set_data(node)
				return
			self.rebalance()

	def get_data(self,ano):
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
						self.node.node = replacement.node
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
