from anosTreeNode import anosTreeNode

class anosTree:
	def __init__(self):
		self.node = None
		self.height = -1
		self.balance = 0;

# TODO - ( anosTreeNode removePais )
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
		if self.node == None:
			newnode = anosTreeNode(ano)
			notDone = newnode.insert(pais,sigla,node)
			self.node = newnode
			self.node.left = anosTree()
			self.node.right = anosTree()
			self.rebalance()
			return notDone
		else:
			if ano < self.node.ano:
				self.node.left.set_data(pais,sigla,ano,node)
			elif ano > self.node.ano:
				self.node.right.set_data(pais,sigla,ano,node)
			elif ano == self.node.ano:
				notDone = self.node.set_data(pais,sigla,node)
				return notDone
			self.rebalance()

	def search(self,ano):
		if self.node == None:
			return None
		if ano > self.node.ano:
			return self.node.right.searchNode(ano)
		elif ano < self.node.ano:
			return self.node.left.searchNode(ano)
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
