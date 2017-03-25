from anosTreePaisesTree import anosTreePaisesTree

class anosTreeNode:
	def __init__(self, ano):
		self.ano = ano
		self.anosTreePaisesTree = anosTreePaisesTree()

	def set_data(self,pais,sigla,node):
		notDone = self.anosTreePaisesTree.insert(pais,sigla,node)
		return notDone

	def get_list_paises(self):
		return self.anosTreePaisesTree.collectPaises([])

	def removePais(self,pais):
		self.anosTreePaisesTree.remove(pais)
