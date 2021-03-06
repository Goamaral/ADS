from anosTree import anosTree
from paisesTree import paisesTree
from dicSiglas import dicSiglas
from hashNumber import hashNumber
from Node import Node

#Mode 0 e Ano !=None: pais e ano
#Mode 1 e Ano !=None: sigla e ano
#Mode 0 e Ano ==None: pais
#Mode 1 e Ano ==None: sigla
#Mode None e Ano !=None: ano

class DuplaArvoreHeader():
	def __init__(self,debugging=True):
		self.dicSiglas = dicSiglas()
		self.anosTree = anosTree()
		self.paisesTree = paisesTree()
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
		newNode = Node(perc)
		notDone = self.anosTree.insert(pais,sigla,ano,newNode)
		if notDone:
			self.paisesTree.insert(pais,sigla,ano,newNode)

	#Permite editar a percentagem de um pais(Sigla dependendo do mode) num determinado ano, devolve None se o pais nao for encontrado
	def edit(self,mode,nome,ano,perc):
		if mode == None:
			raise ValueError('Edicao nao suporta edicao no modo None')
			return
		result = self.searchNode(mode, nome)
		if result == None:
			self.debug('Pais nao encontrado')
			return
		else:
			newNode = Node(perc)
			if mode == 0 or mode == 1:
				result.set_data(ano,newNode)
			else:
				raise ValueError('Modo de edicao nao suportado')

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
			result = self.searchNode(mode, ano)
			if result == None:
				self.debug('Ano nao encontrado')
				return None;
			return result.get_list_paises()

	#Procura o no para o mode e input inseridos
	def searchNode(self,mode,input):
		if mode == 0:
			return self.paisesTree.searchByPais(hashNumber(input))
		elif mode == 1:
			pais = self.translateSigla(input)
			if pais == None:
				return None
			return self.paisesTree.searchByPais(hashNumber(pais))
		elif mode == None:
			return self.anosTree.search(input)
		else:
			raise ValueError('A very specific bad thing happened')

	#Dependendo do mode e das variaveis ano e nome, remove uma percentagem para um ano e pais especifico , ou remove um pais especifico ou um ano especifico
	def remove(self, mode, nome, ano):
		#Se o pais ou sigla forem especificados
		if mode != None:
			#Ano nao especificado = remover pais
			if ano == None:
				#Se o pais foi passado como parametro
				if mode == 0:
					success = self.paisesTree.remove(nome)
					if success != False:
						self.anosTree.removePais(nome)
					else:
						self.debug('Remocao feita sem sucesso')
				#Se foi passado como argumento uma sigla
				elif mode == 1:
					pais = self.translateSigla(nome)
					success = self.paisesTree.remove(pais)
					if success != False:
						self.anosTree.removePais(pais)
					else:
						self.debug('Remocao feita sem sucesso')
				else:
					raise ValueError('Modo nao suportado - modo nao suportado com ano nao especificado')
			#Ano especificado
			else:
				#Se o pais ou sigla foi passado como parametro
				if mode == 0 or mode == 1:
					result = self.searchNode(mode,nome)
					node = Node(None)
					if result != None:
						result.set_data(ano,node)
					else:
						self.debug('Pais nao encontrado')
				else:
					raise ValueError('Modo nao suportado - modo nao suportado com ano especificado')
		#modo ano = remover ano
		else:
			success = self.anosTree.remove(ano)
			if success != False:
				self.paisesTree.removeAno(ano)
			else:
				self.debug('Remocao feita sem sucesso')
