from AvlTree import AvlTree
from dicSiglas import dicSiglas

debugging = True

def debug(msg):
	if debugging:
		print msg

#Mode 0 e Ano !=None: pais e ano
#Mode 1 e Ano !=None: sigla e ano
#Mode 0 e Ano ==None: pais
#Mode 1 e Ano ==None: sigla
#Mode None e Ano !=None: ano

class AvlHeader():
	def __init__(self):
		self.dicSiglas = dicSiglas()
		self.tree = AvlTree()

	#Devolve pais associado a sigla. Se a sigla nao existir devolve None
	def translateSigla(self, input):
		result = self.dicSiglas.search(input)
		if result == None:
			debug('Sigla nao encontrada')
		return result

	#Atualiza o dicionario de siglas com o par sigla pais
	def addToSiglaDictionary(self, sigla, pais):
		self.dicSiglas.add(sigla,pais)

	#Permite adicionar percentagem para um pais num ano, quer o pais exista ou nao
	#Nao achamos relevante inserir um ano sem dados ou um pais sem dados
	def insert(self,pais,sigla,ano,perc):
		self.addToSiglaDictionary(sigla, pais)
		self.tree.insert(pais,sigla,ano,perc)

	#Permite editar a percentagem de um pais(Sigla dependendo do mode) num determinado ano, devolve None se o pais nao for encontrado
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
			return self.tree.collectPaisesAno(ano,[])

	#Procura o no para o mode e input inseridos
	def searchNode(self,mode,input):
		if mode == 0:
			return self.tree.searchByPais(hash(input))
		else:
			pais = self.translateSigla(input)
			if pais == None:
				return None
			return self.tree.searchByPais(hash(pais))

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
