from anosTreeNode import anosTreeNode

class anosTree:
	def __init__(self):
		self.node = None
		self.height = -1
		self.balance = 0;

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
