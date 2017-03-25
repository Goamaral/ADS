from anosTreeNode import anosTreeNode

class anosTree:
	def __init__(self):
		self.node = None
		self.height = -1
		self.balance = 0;

	def removePais(self,pais):
		if self.node != None:
			self.node.removePais(pais)
			right = self.node.right != None
			left = self.node.left != None
			if right and left:
				self.node.left.removePais(pais)
				self.node.right.removePais(pais)
			elif right:
				self.node.right.removePais(pais)
			elif left:
				self.node.left.removePais(pais)
			else:
				raise ValueError('Erro inesperado na remocao do pais na arvore dos anos')


	def insert(self,pais,sigla,ano,node):
		notDone = None
		if self.node == None:
			newnode = anosTreeNode(ano)
			notDone = newnode.set_data(pais,sigla,node)
			self.node = newnode
			self.node.left = anosTree()
			self.node.right = anosTree()
		else:
			if ano < self.node.ano:
				notDone = self.node.left.insert(pais,sigla,ano,node)
			elif ano > self.node.ano:
				notDone = self.node.right.insert(pais,sigla,ano,node)
			elif ano == self.node.ano:
				notDone = self.node.set_data(pais,sigla,node)

		self.rebalance()
		if notDone != None and notDone != 0:
			return notDone

	def search(self,ano):
		if self.node == None:
			return None
		if ano > self.node.ano:
			return self.node.right.search(ano)
		elif ano < self.node.ano:
			return self.node.left.search(ano)
		else:
			return self.node

	def remove(self, input):
		if self.node != None:
			if self.node.ano == input:
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
						self.node.anosTreePaisesTree = replacement.anosTreePaisesTree
						self.node.right.remove(replacement.ano)

				self.rebalance()
				return
			elif input < self.node.ano:
				self.node.left.remove(input)
			elif input > self.node.ano:
				self.node.right.remove(input)

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
