from ListaCirculasDuplamenteLigada import ListaCirculasDuplamenteLigada as List
from AVL import treeHeader as Avl
import csv
import time

#DOING:
	#TODO: pesquisar anos pais
#TODO: remover pais
#TODO: remover ano
#TODO: pesquisar paises ano
#TODO: usar hash para as siglas
#TODO: inserir alfabeticamente na lista
#TODO: criar no com a media atual

#TODO: estrutura focada em complexidade espacial

debugging = True

def debug(msg):
	if debugging:
		print msg

	'''
	OUTPUT ESPERADO:
	None
	None
	100.0
	100.0
	Pais nao encontrado
	Pais nao encontrado
	20
	20
	50
	50
	Pais nao encontrado
	Pais nao encontrado
	None
	None
	None
	None
	Portugal
	{1990: None}
	{1100: None}
	{2000: 100.0}
	{1110: None}
	{2010: 100.0}
	{2012: 100.0}
	PRT
	{1990: None}
	{1100: None}
	{2000: 100.0}
	{1110: None}
	{2010: 100.0}
	{2012: 100.0}
	Pais nao encontrado
	None
	Pais nao encontrado
	None
	1990
	{'Germany': 100.0}
	{'Belgium': 100.0}
	{'United Arab Emirates': 87.22775}
	...
	1100
	[]
	Pais nao encontrado
	None
	Pais nao encontrado
	None
	Pais nao encontrado
	None
	Pais nao encontrado
	None
	1990
	[]
	1100
	[]

	'''

def beautifyListPrint(l,title):
	if l == None:
		print None
		return
	print title
	if l == []:
		print '[]'
		return
	for item in l:
		print item

def main():
	#Escolher estrutura de dados
	#List - Lista duplamente ligada circular
	#Avl - Arvore binaria de pesquisa balanceada personalizada
	#
	es = Avl()

	#Tratar dados do ficheito dados.csv
	tratamento_de_dados(es)

	#pesquisa insercao edicao remocao
	start = time.time()
	#Procurar ano nao existente
	#Por sigla
	debug(es.search(1, 'PRT', 1950))
	#Por pais
	debug(es.search(0, 'Portugal', 1950))

	#Procurar ano existente
	#Por sigla
	debug(es.search(1, 'PRT', 1990))
	#Por pais
	debug(es.search(0, 'Portugal', 1990))

	#Editar pais nao existente
	es.edit(1,'XP',1990,10)
	es.edit(0,'Xponent',1990,10)

	#Editar pais existente e data inexistente
	es.edit(1,'PRT',1100,10)
	es.edit(0,'Portugal',1110,10)

	#Editar pais existente e data existente
	es.edit(1,'PRT',1990,20)
	debug(es.search(1, 'PRT', 1990))
	debug(es.search(0, 'Portugal', 1990))
	es.edit(0,'Portugal',1990,50)
	debug(es.search(1, 'PRT', 1990))
	debug(es.search(0, 'Portugal', 1990))

	#Remover pais nao existente
	es.remove(1,'XP',1990)
	es.remove(0,'Xponent',1990)

	#Remover pais existente e data inexistente
	es.remove(1,'PRT',1100)
	es.remove(0,'Portugal',1110)

	#Remover pais existente e data existente
	es.remove(1,'PRT',1990)
	debug(es.search(1, 'PRT', 1990))
	debug(es.search(0, 'Portugal', 1990))
	es.remove(0,'Portugal',1990)
	debug(es.search(1, 'PRT', 1990))
	debug(es.search(0, 'Portugal', 1990))

	#listar anos de um pais
	#pais existente
	beautifyListPrint(es.search(0, 'Portugal', None), 'Portugal')
	beautifyListPrint(es.search(1, 'PRT', None), 'PRT')
	#pais inexistente, ano existente
	beautifyListPrint(es.search(0, 'Xponent', None), 'Xponent')
	beautifyListPrint(es.search(1, 'XP', None), 'XP')

	#listar paises de um ano
	#ano existente
	beautifyListPrint(es.search(None, None, 1990), '1990')
	#ano inexistente, ano existente
	beautifyListPrint(es.search(None, None, 1100), '1100')

	#remover pais
	#pais existente
	es.remove(0, 'Portugal', None)
	debug(es.search(0, 'Portugal', None))
	debug(es.search(1, 'PRT', None))
	#pais inexistente
	es.remove(0, 'Xponent', None)
	debug(es.search(0, 'Xponent', None))
	debug(es.search(1, 'XP', None))

	#remover ano
	#ano existente
	es.remove(None, None, 1990)
	beautifyListPrint(es.search(None, None, 1990), '1990')
	#ano inexistente
	es.remove(None, None, 1100)
	beautifyListPrint(es.search(None, None, 1100), '1100')

	end = time.time()

	#print str(end-start)

def tratamento_de_dados(es):
	rows = []

	with open('dados.csv', 'rb') as csvfile:
		spamreader = csv.reader(csvfile)
		for row in spamreader:
			rows.append(row[0].split(';'))

	#limpa csv
	for i in range(len(rows)):
		row = rows[i]
		for j in range(len(row)):
			row[j] = row[j].replace('"', '')

	#Obtem o header
	header = rows[0]

	#Obtem lista de anos
	listaAnos = header[2:]

	#Remove header
	rows = rows[1:]

	for row in rows:
		pais = row[0]
		sigla = row[1]
		anos = row[2:]
		for i in range(len(anos)):
			perc = anos[i]
			ano = listaAnos[i]
			if perc != '':
				ano = int(ano)
				perc = float(perc)
				es.insert(pais,sigla,ano,perc)

if __name__ == "__main__":
	main()
