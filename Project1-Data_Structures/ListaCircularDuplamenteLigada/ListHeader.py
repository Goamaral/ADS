from List import List
from hashNumber import hashNumber
from dicSiglas import dicSiglas

debugging = True

class ListHeader:
	def __init__(self,debugging):
		self.middleNode = None
		self.secondMiddleNode = None
		self.middle = 0
		self.nNodes = 0
		self.list = List()
		self.dicSiglas = dicSiglas()
		self.debugging = debugging

	def debug(self,msg):
		if self.debugging:
			print msg

	#Devolve pais associado a sigla. Se a sigla nao existir devolve None
	def translateSigla(self, input):
		result = self.dicSiglas.search(input)
		if result == None:
			self.debug('Sigla nao encontrada')
		return result

	#Atualiza o dicionario de siglas com o par sigla pais
	def addToSiglaDictionary(self, sigla, pais):
		self.dicSiglas.add(sigla,pais)

	#Permite adicionar percentagem para um pais num ano, quer o pais exista ou nao
	#Nao achamos relevante inserir um ano sem dados ou um pais sem dados
	def insert(self,pais,sigla,ano,perc):
		self.addToSiglaDictionary(sigla, pais)
		(isNewNode, newNode, msg) = self.list.insert(pais,sigla,ano,perc)
		if isNewNode:
			if self.middleNode == None:
				self.middleNode = newNode
			elif self.nNodes % 2 != 0:
				if newNode.hashPais > self.middleNode.hashPais:
					self.secondMiddleNode = newNode
				elif newNode.hashPais < self.middleNode.hashPais:
					backup = self.middleNode
					self.middleNode = newNode
					self.secondMiddleNode = backup
				else:
					raise ValueError('Erro no calculo da mediana (nNodes impar)')
				self.middle = (self.middleNode.hashPais + self.secondMiddleNode.hashPais) / 2
			else:
				#centro
				if newNode.hashPais > self.middleNode.hashPais and newNode.hashPais < self.secondMiddleNode.hashPais:
					self.secondMiddleNode = None
					self.middleNode = newNode
				#esquerda
				elif newNode.hashPais > self.secondMiddleNode.hashPais:
					backup = self.secondMiddleNode
					self.secondMiddleNode = None
					self.middleNode = backup
				#direita
				elif newNode.hashPais < self.middleNode.hashPais:
					backup = self.middleNode
					self.secondMiddleNode = None
					self.middleNode = backup
				else:
					raise ValueError('Erro no calculo da mediana (nNodes par)')

				self.middle = self.middleNode.hashPais

			self.nNodes = self.nNodes + 1

	#Permite editar a percentagem de um pais(Sigla dependendo do mode) num determinado ano, devolve None se o pais ou o ano nao for encontrado
	def edit(self,mode,nome,ano,perc):
		result = self.searchNode(mode, nome)
		if result == None:
			self.debug('Pais nao encontrado')
			return None
		else:
			return result.set_data(ano,perc)

	#Dependendo do mode e as variaveis ano e nome, devolve a percentagem para um pais(Sigla) num determinado ano, uma lista dos paises num determinado ano ou uma lista dos anos de um determinado pais
	def search(self, mode, nome, ano):
		if mode != None:
			result = self.searchNode(mode, nome)
			if result == None:
				self.debug('Pais nao encontrado')
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
	def searchNode(self, mode, nome):
		current = self.list.head
		if current == None:
			return None

		if mode == 0:
			pais = nome
		else:
			pais = self.translateSigla(nome)
			if pais == None:
				return None

		hashCode = hashNumber(pais)

		if hashCode > self.middle:
			return self.list.leftSearch(hashCode)
		else:
			return self.list.rightSearch(hashCode)


	#Dependendo do mode e das variaveis ano e nome, remove uma percentagem para um ano e pais especifico , ou remove um pais especifico ou um ano especifico
	def remove(self, mode, nome, ano):
		if mode != None:
			result = self.searchNode(mode, nome)
			if ano != None:
				if result != None:
					result.set_data(ano,None)
				else:
					self.debug('Pais nao encontrado')
			else:
				#remover um pais
				if result != None:
					if self.nNodes % 2 != 0:
						self.middleNode = result.prev
						self.secondMiddleNode = result.next
						self.middle = (self.middleNode.hashPais + self.searchNode.hashPais) / 2
					else:
						if result.hashPais > self.middleNode.hashPais:
							self.secondMiddleNode = None
						elif result.hashPais < self.secondMiddleNode:
							backup = self.secondMiddleNode
							self.secondMiddleNode = None
							self.middleNode = backup
						else:
							raise ValueError('Erro no calculo da mediana (nNodes par)')

						self.middle = self.middleNode.hashPais

					self.list.removeNode(result)
					self.nNodes = self.nNodes - 1

				else:
					self.debug('Pais nao encontrado')
		else:
			#remover um ano
			self.list.removeAno(ano)
