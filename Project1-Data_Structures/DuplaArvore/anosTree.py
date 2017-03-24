from anosTreeNode import anosTreeNode

class anosTree:
	def __init__(self):
		self.node = None
		self.height = -1
		self.balance = 0;

#TODO - ( anosTreeNode setdata )
	def insert(self,pais,sigla,ano,node):
		newnode = anosTreeNode(ano)

		if self.node == None:
			newnode.set_data(pais,sigla,node)
			self.node = newnode
			self.node.left = anosTree()
			self.node.right = anosTree()
		else:
			if ano < self.node.ano:
				self.node.left.insert(pais,sigla,ano,node)
			elif ano > self.node.ano:
				self.node.right.insert(pais,sigla,ano,node)
			elif ano == self.node.ano:
				self.node.set_data(pais,sigla,perc)
				return

		self.rebalance()
