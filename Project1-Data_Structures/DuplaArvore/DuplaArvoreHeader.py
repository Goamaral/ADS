from anosTree import anosTree
from paisesTree import paisTree
from dicSiglas import dicSiglas
from hashNumber import hashNumber
from Node import Node

debugging = True

def debug(msg):
	if debugging:
		print msg

#Mode 0 e Ano !=None: pais e ano
#Mode 1 e Ano !=None: sigla e ano
#Mode 0 e Ano ==None: pais
#Mode 1 e Ano ==None: sigla
#Mode None e Ano !=None: ano

class DuplaArvoreHeader():
	def __init__(self):
		self.dicSiglas = dicSiglas()
		self.anosTree = anosTree()
		self.paisesTree = paisesTree()

	#Devolve pais associado a sigla. Se a sigla nao existir devolve None
	def translateSigla(self, input):
		result = self.dicSiglas.search(input)
		if result == None:
			debug('Sigla nao encontrada')
		return result

	#Atualiza o dicionario de siglas com o par sigla pais
	def addToSiglaDictionary(self, sigla, pais):
		self.dicSiglas.add(sigla,pais)

#TODO - IN ( Node init, paises tree insert, anos tree insert )
	#Permite adicionar percentagem para um pais num ano, quer o pais exista ou nao
	#Nao achamos relevante inserir um ano sem dados ou um pais sem dados
	def insert(self,pais,sigla,ano,perc):
		self.addToSiglaDictionary(sigla, pais)
		newNode = Node(perc)
		#TODO return if sucessful
		self.anosTree.insert(pais,sigla,ano,newNode)
		self.paisesTree.insert(pais,sigla,ano,newNode)

#TODO - IN ( self searchNode, Node setdata )
	#Permite editar a percentagem de um pais(Sigla dependendo do mode) num determinado ano, devolve None se o pais nao for encontrado
	def edit(self,mode,nome,ano,perc):
		if mode == None:
			return
		result = self.searchNode(mode, nome)
		if result == None:
			debug('Pais nao encontrado')
			return
		else:
			result.set_data(ano,perc)

#TODO - IN ( self searchNode, pais getdata, pais getlistanos, ano getlistpaises )
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
			result = self.searchNode(mode, ano)
			if result == None:
				debug('Ano nao encontrado')
				return None;
			return result.get_list_paises()

#TODO - IN ( paisesTree searchByPais, anosTree search )
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

#TODO - IN ( self searchNode, pais setdata, pais remove )
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
				success = self.paisesTree.remove(nome)
				if success == False:
					debug('Pais nao encontrado')
		else:
			#remover um ano
			if ano == None:
				return None
			success = self.anosTree.remove(ano)
			if success == False:
				debug('Ano nao encontrado')