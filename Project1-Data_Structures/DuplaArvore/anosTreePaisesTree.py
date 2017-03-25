from anosTreePaisesTreeNode import anosTreePaisesTreeNode

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
				return
			elif input < self.node.ano:
				self.node.left.remove(input)
			elif input > self.node.ano:
				self.node.right.remove(input)

			self.rebalance()

		return False

	def insert(self,pais,sigla,node):
		if self.node == None:
			newnode = anosTreePaisesTreeNode(pais,sigla)
			notDone = newnode.set_data(node)
			self.node = newnode
			self.node.left = anosTreePaisesTree()
			self.node.right = anosTreePaisesTree()
			self.rebalance()
			return notDone
		else:
			if ano < self.node.ano:
				self.node.left.insert(pais,sigla,node)
			elif ano > self.node.ano:
				self.node.right.insert(pais,sigla,node)
			elif ano == self.node.ano:
				notDone = self.node.set_data(node)
				return notDone
			self.rebalance()

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
