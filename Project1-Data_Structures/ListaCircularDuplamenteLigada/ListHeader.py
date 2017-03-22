from List import List

class ListHeader:
	def __init__(self):
		self.average = 0
		self.sum = 0
		self.nNodes = 0
		self.list = List()

	#Permite adicionar percentagem para um pais num ano, quer o pais exista ou nao
	#Nao achamos relevante inserir um ano sem dados ou um pais sem dados
	def insert(self,pais,sigla,ano,perc):
		isNewNode = self.list.insert(pais,sigla,ano,perc)
		if isNewNode:
			self.nNodes = self.nNodes + 1
			self.sum = self.sum + ord(pais[0]) - ord('a') + 1
			self.average = self.sum / self.nNodes

	#Permite editar a percentagem de um pais(Sigla dependendo do mode) num determinado ano, devolve None se o pais ou o ano nao for encontrado
	def edit(self,mode,nome,ano,perc):
		result = self.searchNode(mode, nome)
		if result == None:
			debug('Pais nao encontrado')
			return None
		else:
			return result.set_data(ano,perc)

	#Dependendo do mode e as variaveis ano e nome, devolve a percentagem para um pais(Sigla) num determinado ano, uma lista dos paises num determinado ano ou uma lista dos anos de um determinado pais
	def search(self, mode, nome, ano):
		if mode != None:
			result = self.searchNode(mode, nome)
			if result == None:
				debug('Pais nao encontrado')
				return None;
			if ano != None:
				return result.get_data(ano)
			else:
				#listar anos de um pais
				return result.get_list_anos()
		else:
			#listar todos os paises de um ano
			if ano == None:
				return None
			return self.list.collectPaisesAno(ano,[])

	#Procura o no para o mode e input inseridos
	def searchNode(self,mode,input):
		if mode == 0:
			return self.list.searchByPais(hash(input))
		else:
			return self.list.searchBySigla(hash(input))

	#Dependendo do mode e das variaveis ano e nome, remove uma percentagem para um ano e pais especifico , ou remove um pais especifico ou um ano especifico
	def remove(self, mode, nome, ano):
		if mode != None:
			if ano != None:
				result = self.searchNode(mode, nome)
				if result != None:
					result.set_data(ano,None)
				else:
					debug('Pais nao encontrado')
			else:
				if mode == 1:
					nome = self.translateSigla(nome)
				#remover um pais
				self.tree.remove(nome)
		else:
			#remover um ano
			self.tree.removeAno(ano)
