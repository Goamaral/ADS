from ListaCircularDuplamenteLigada.ListHeader import ListHeader as List
from AVL.AvlHeader import AvlHeader as Avl
from DuplaArvore.DuplaArvoreHeader import DuplaArvoreHeader as DoubleAvl
import csv
import timeit
from hashNumber import hashNumber

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

def benchmark(fun, *args):
	times = []
	for i in range(10000):
		start = timeit.default_timer()
		fun(*args)
		end = timeit.default_timer()
		times.append(end-start)
	return sum(times) / 10000

def menu(input):
	print '--------------------------------------------------'
	(title, options) = input
	print title
	_options = sorted(options.keys())
	for option in _options:
		print str(option) + ': ' + str(options[option])

	op = raw_input('Opcao: ')
	if op in options.keys():
		return op
	else:
		print 'Opcao invalida'
		return menu(input)

menu_principal = ('Escolha a estrutura a usar', {'0':'Avl de paises com Avl de anos em cada no','1':'Dupla Avl, Avl de paises com Avl de anos em cada no e Avl de anos com Avl de paises em cada no','2':'Lista circular duplamente ligada de paises com Avl de anos em cada no'})

menu_principal_es = ('Menu principal', {'0':'Normal - Prints nao mutados','1':'Benchmarks - Prints mutados e cada operacao ira ser corrida 10000 vezes para obter medias'})

menu_normal_es = ('Menu', {'0':'Pesquisar','1':'Editar','2':'Remover','3':'Inserir'})
menu_pesquisa = ('Pesquisar percentagem:', {'0':'Pais num ano (Portugal em 1950)','1':'Sigla num ano (PRT em 1950)','2':'Num ano (Percentagens de 1950)','3':'Segundo pais (Percentagens de Portugal)','4':'Segundo sigla (Percentagens de PRT)'})
menu_editar = ('Editar percentagem:', {'0':'Pais num ano (Portugal em 1950)','1':'Sigla num ano (PRT em 1950)'})
menu_remover = ('Remover', {'0':'Percentagem de pais num ano (Portugal em 1950)','1':'Percentagem de sigla num ano (PRT em 1950)','2':'Um ano (Percentagens de 1950)','3':'Um pais (Portugal)','4':'Um pais segundo  sigla (PRT)'})

menu_benchmarks_es = ('Menu Benchmarks', {'0':'Pesquisar','1':'Editar','2':'Remover','3':'Inserir'})

def menu_logic():
	es_op = menu(menu_principal)
	op = menu(menu_principal_es)
	es = menu_principal_es_logic(es_op,op)

	if op == '0':
		menu_normal_es_op = menu(menu_normal_es)
		menu_normal_es_logic(menu_normal_es_op, es)
	elif op == '1':
		menu_benchmarks_es_op = menu(menu_benchmarks_es)
		menu_benchmarks_es_logic(menu_benchmarks_es_op, es)

def menu_principal_es_logic(es_op,op):
	if op == '0' and es_op == '0':
		es = Avl()
	elif op == '1' and es_op == '0':
		es = Avl(False)
	elif op == '0' and es_op == '1':
		es = DoubleAvl()
	elif op == '1' and es_op == '1':
		es = DoubleAvl(False)
	elif op == '0' and es_op == '2':
		es = List()
	elif op == '1' and es_op == '2':
		es = List(False)
	tratamento_de_dados(es)
	return es

def menu_normal_es_logic(menu_normal_es_op,es):
	if menu_normal_es_op == '0':
		menu_pesquisa_op = menu(menu_pesquisa)
		if menu_pesquisa_op == '0':
			print '--------------------------------------------------'
			pais = raw_input('Pais (Case sensitive): ')
			ano_str = raw_input('Ano: ')
			try:
				ano = int(ano_str)
			except ValueError:
				print 'Opcao Invalida'
				new_menu_normal_es_op = menu(menu_normal_es)
				menu_normal_es_logic(new_menu_normal_es_op,es)
				return
			print es.search(0,pais,ano)
			new_menu_normal_es_op = menu(menu_normal_es)
			menu_normal_es_logic(new_menu_normal_es_op,es)
		elif menu_pesquisa_op == '1':
			print '--------------------------------------------------'
			sigla = raw_input('Sigla (Case sensitive - All Caps): ')
			ano_str = raw_input('Ano: ')
			try:
				ano = int(ano_str)
			except ValueError:
				print 'Opcao Invalida'
				new_menu_normal_es_op = menu(menu_normal_es)
				menu_normal_es_logic(new_menu_normal_es_op,es)
				return
			print es.search(1,sigla,ano)
			new_menu_normal_es_op = menu(menu_normal_es)
			menu_normal_es_logic(new_menu_normal_es_op,es)
		elif menu_pesquisa_op == '2':
			print '--------------------------------------------------'
			ano_str = raw_input('Ano: ')
			try:
				ano = int(ano_str)
			except ValueError:
				print 'Opcao Invalida'
				new_menu_normal_es_op = menu(menu_normal_es)
				menu_normal_es_logic(new_menu_normal_es_op,es)
				return
			beautifyListPrint(es.search(None,None,ano), ano)
			new_menu_normal_es_op = menu(menu_normal_es)
			menu_normal_es_logic(new_menu_normal_es_op,es)
		elif menu_pesquisa_op == '3':
			print '--------------------------------------------------'
			pais = raw_input('Pais (Case sensitive): ')
			beautifyListPrint(es.search(0,pais,None), pais)
			new_menu_normal_es_op = menu(menu_normal_es)
			menu_normal_es_logic(new_menu_normal_es_op,es)
		elif menu_pesquisa_op == '4':
			print '--------------------------------------------------'
			sigla = raw_input('Sigla (Case sensitive - All Caps): ')
			beautifyListPrint(es.search(1,sigla,None), sigla)
			new_menu_normal_es_op = menu(menu_normal_es)
			menu_normal_es_logic(new_menu_normal_es_op,es)
	elif menu_normal_es_op == '1':
		menu_editar_op = menu(menu_editar)
		if menu_editar_op == '0':
			print '--------------------------------------------------'
			pais = raw_input('Pais (Case sensitive): ')
			ano_str = raw_input('Ano: ')
			try:
				ano = int(ano_str)
			except ValueError:
				print 'Opcao Invalida'
				new_menu_normal_es_op = menu(menu_normal_es)
				menu_normal_es_logic(new_menu_normal_es_op,es)
				return
			perc_str = raw_input('Percentagem: ')
			try:
				perc = int(perc_str)
			except ValueError:
				print 'Opcao Invalida'
				new_menu_normal_es_op = menu(menu_normal_es)
				menu_normal_es_logic(new_menu_normal_es_op,es)
				return
			es.edit(0,pais,ano,perc)
			new_menu_normal_es_op = menu(menu_normal_es)
			menu_normal_es_logic(new_menu_normal_es_op,es)
		elif menu_editar_op == '1':
			print '--------------------------------------------------'
			sigla = raw_input('Sigla (Case sensitive - All Caps): ')
			ano_str = raw_input('Ano: ')
			try:
				ano = int(ano_str)
			except ValueError:
				print 'Opcao Invalida'
				new_menu_normal_es_op = menu(menu_normal_es)
				menu_normal_es_logic(new_menu_normal_es_op,es)
				return
			perc_str = raw_input('Percentagem: ')
			try:
				perc = int(perc_str)
			except ValueError:
				print 'Opcao Invalida'
				new_menu_normal_es_op = menu(menu_normal_es)
				menu_normal_es_logic(new_menu_normal_es_op,es)
				return
			es.edit(1,sigla,ano,perc)
			new_menu_normal_es_op = menu(menu_normal_es)
			menu_normal_es_logic(new_menu_normal_es_op,es)
	elif menu_normal_es_op == '2':
		menu_remover_op = menu(menu_remover)
		if menu_remover_op == '0':
			print '--------------------------------------------------'
			pais = raw_input('Pais (Case sensitive): ')
			ano_str = raw_input('Ano: ')
			try:
				ano = int(ano_str)
			except ValueError:
				print 'Opcao Invalida'
				new_menu_normal_es_op = menu(menu_normal_es)
				menu_normal_es_logic(new_menu_normal_es_op,es)
				return
			es.remove(0,pais,ano)
			new_menu_normal_es_op = menu(menu_normal_es)
			menu_normal_es_logic(new_menu_normal_es_op,es)
		elif menu_remover_op == '1':
			print '--------------------------------------------------'
			sigla = raw_input('Sigla (Case sensitive - All Caps): ')
			ano_str = raw_input('Ano: ')
			try:
				ano = int(ano_str)
			except ValueError:
				print 'Opcao Invalida'
				new_menu_normal_es_op = menu(menu_normal_es)
				menu_normal_es_logic(new_menu_normal_es_op,es)
				return
			es.remove(1,sigla,ano)
			new_menu_normal_es_op = menu(menu_normal_es)
			menu_normal_es_logic(new_menu_normal_es_op,es)
		elif menu_remover_op == '2':
			print '--------------------------------------------------'
			ano_str = raw_input('Ano: ')
			try:
				ano = int(ano_str)
			except ValueError:
				print 'Opcao Invalida'
				new_menu_normal_es_op = menu(menu_normal_es)
				menu_normal_es_logic(new_menu_normal_es_op,es)
				return
			es.remove(None,None,ano)
			new_menu_normal_es_op = menu(menu_normal_es)
			menu_normal_es_logic(new_menu_normal_es_op,es)
		elif menu_remover_op == '3':
			print '--------------------------------------------------'
			pais = raw_input('Pais (Case sensitive): ')
			es.remove(0,pais,None)
			new_menu_normal_es_op = menu(menu_normal_es)
			menu_normal_es_logic(new_menu_normal_es_op,es)
		elif menu_remover_op == '4':
			print '--------------------------------------------------'
			sigla = raw_input('Sigla (Case sensitive - All Caps): ')
			es.remove(1,sigla,None)
			new_menu_normal_es_op = menu(menu_normal_es)
			menu_normal_es_logic(new_menu_normal_es_op,es)
	elif menu_normal_es_op == '3':
		print '--------------------------------------------------'
		pais = raw_input('Pais (Case sensitive): ')
		sigla = raw_input('Sigla (Case sensitive - All caps): ')
		ano_str = raw_input('Ano: ')
		try:
			ano = int(ano_str)
		except ValueError:
			print 'Opcao Invalida'
			new_menu_normal_es_op = menu(menu_normal_es)
			menu_normal_es_logic(new_menu_normal_es_op,es)
			return
		perc_str = raw_input('Percentagem: ')
		try:
			perc = int(ano_str)
		except ValueError:
			print 'Opcao Invalida'
			new_menu_normal_es_op = menu(menu_normal_es)
			menu_normal_es_logic(new_menu_normal_es_op,es)
			return
		es.insert(pais,sigla,ano,perc)
		new_menu_normal_es_op = menu(menu_normal_es)
		menu_normal_es_logic(new_menu_normal_es_op,es)

def menu_benchmarks_es_logic(menu_benchmarks_es_op,es):
	if menu_benchmarks_es_op == '0':
		menu_pesquisa_op = menu(menu_pesquisa)
		if menu_pesquisa_op == '0':
			print '--------------------------------------------------'
			pais = raw_input('Pais (Case sensitive): ')
			ano_str = raw_input('Ano: ')
			try:
				ano = int(ano_str)
			except ValueError:
				print 'Opcao Invalida'
				new_menu_benchmarks_es_op = menu(menu_benchmarks_es)
				menu_benchmarks_es_logic(new_menu_benchmarks_es_op,es)
				return
			print benchmark(es.search,0,pais,ano)
			new_menu_benchmarks_es_op = menu(menu_benchmarks_es)
			menu_menu_benchmarks_es_logic(new_menu_benchmarks_es_op,es)
		elif menu_pesquisa_op == '1':
			print '--------------------------------------------------'
			sigla = raw_input('Sigla (Case sensitive - All Caps): ')
			ano_str = raw_input('Ano: ')
			try:
				ano = int(ano_str)
			except ValueError:
				print 'Opcao Invalida'
				new_menu_benchmarks_es_op = menu(menu_benchmarks_es)
				menu_menu_benchmarks_es_logic(new_menu_benchmarks_es_op,es)
				return
			print benchmark(es.search,1,sigla,ano)
			new_menu_benchmarks_es_op = menu(menu_benchmarks_es)
			menu_menu_benchmarks_es_logic(new_menu_benchmarks_es_op,es)
		elif menu_pesquisa_op == '2':
			print '--------------------------------------------------'
			ano_str = raw_input('Ano: ')
			try:
				ano = int(ano_str)
			except ValueError:
				print 'Opcao Invalida'
				new_menu_benchmarks_es_op = menu(menu_benchmarks_es)
				menu_menu_benchmarks_es_logic(new_menu_benchmarks_es_op,es)
				return
			print benchmark(es.search,None,None,ano)
			new_menu_benchmarks_es_op = menu(menu_benchmarks_es)
			menu_menu_benchmarks_es_logic(new_menu_benchmarks_es_op,es)
		elif menu_pesquisa_op == '3':
			print '--------------------------------------------------'
			pais = raw_input('Pais (Case sensitive): ')
			print benchmark(es.search,0,pais,None)
			new_menu_benchmarks_es_op = menu(menu_benchmarks_es)
			menu_menu_benchmarks_es_logic(new_menu_benchmarks_es_op,es)
		elif menu_pesquisa_op == '4':
			print '--------------------------------------------------'
			sigla = raw_input('Sigla (Case sensitive - All Caps): ')
			print benchmark(es.search,1,sigla,None)
			new_menu_benchmarks_es_op = menu(menu_benchmarks_es)
			menu_menu_benchmarks_es_logic(new_menu_benchmarks_es_op,es)
	elif menu_benchmarks_es_op == '1':
		menu_editar_op = menu(menu_editar)
		if menu_editar_op == '0':
			print '--------------------------------------------------'
			pais = raw_input('Pais (Case sensitive): ')
			ano_str = raw_input('Ano: ')
			try:
				ano = int(ano_str)
			except ValueError:
				print 'Opcao Invalida'
				new_menu_benchmarks_es_op = menu(menu_benchmarks_es)
				menu_menu_benchmarks_es_logic(new_menu_benchmarks_es_op,es)
				return
			perc_str = raw_input('Percentagem: ')
			try:
				perc = int(perc_str)
			except ValueError:
				print 'Opcao Invalida'
				new_menu_benchmarks_es_op = menu(menu_benchmarks_es)
				menu_menu_benchmarks_es_logic(new_menu_benchmarks_es_op,es)
				return
			print benchmark(es.edit,0,pais,ano,perc)
			new_menu_benchmarks_es_op = menu(menu_benchmarks_es)
			menu_menu_benchmarks_es_logic(new_menu_benchmarks_es_op,es)
		elif menu_editar_op == '1':
			print '--------------------------------------------------'
			sigla = raw_input('Sigla (Case sensitive - All Caps): ')
			ano_str = raw_input('Ano: ')
			try:
				ano = int(ano_str)
			except ValueError:
				print 'Opcao Invalida'
				new_menu_benchmarks_es_op = menu(menu_benchmarks_es)
				menu_menu_benchmarks_es_logic(new_menu_benchmarks_es_op,es)
				return
			perc_str = raw_input('Percentagem: ')
			try:
				perc = int(perc_str)
			except ValueError:
				print 'Opcao Invalida'
				new_menu_benchmarks_es_op = menu(menu_benchmarks_es)
				menu_menu_benchmarks_es_logic(new_menu_benchmarks_es_op,es)
				return
			print benchmark(es.edit,1,sigla,ano,perc)
			new_menu_benchmarks_es_op = menu(menu_benchmarks_es)
			menu_menu_benchmarks_es_logic(new_menu_benchmarks_es_op,es)
	elif menu_benchmarks_es_op == '2':
		menu_remover_op = menu(menu_remover)
		if menu_remover_op == '0':
			print '--------------------------------------------------'
			pais = raw_input('Pais (Case sensitive): ')
			ano_str = raw_input('Ano: ')
			try:
				ano = int(ano_str)
			except ValueError:
				print 'Opcao Invalida'
				new_menu_benchmarks_es_op = menu(menu_benchmarks_es)
				menu_menu_benchmarks_es_logic(new_menu_benchmarks_es_op,es)
				return
			print benchmark(es.remove,0,pais,ano)
			new_menu_benchmarks_es_op = menu(menu_benchmarks_es)
			menu_menu_benchmarks_es_logic(new_menu_benchmarks_es_op,es)
		elif menu_remover_op == '1':
			print '--------------------------------------------------'
			sigla = raw_input('Sigla (Case sensitive - All Caps): ')
			ano_str = raw_input('Ano: ')
			try:
				ano = int(ano_str)
			except ValueError:
				print 'Opcao Invalida'
				new_menu_benchmarks_es_op = menu(menu_benchmarks_es)
				menu_menu_benchmarks_es_logic(new_menu_benchmarks_es_op,es)
				return
			print benchmark(es.remove,1,sigla,ano)
			new_menu_benchmarks_es_op = menu(menu_benchmarks_es)
			menu_menu_benchmarks_es_logic(new_menu_benchmarks_es_op,es)
		elif menu_remover_op == '2':
			print '--------------------------------------------------'
			ano_str = raw_input('Ano: ')
			try:
				ano = int(ano_str)
			except ValueError:
				print 'Opcao Invalida'
				new_menu_benchmarks_es_op = menu(menu_benchmarks_es)
				menu_menu_benchmarks_es_logic(new_menu_benchmarks_es_op,es)
				return
			print benchmark(es.remove,None,None,ano)
			new_menu_benchmarks_es_op = menu(menu_benchmarks_es)
			menu_menu_benchmarks_es_logic(new_menu_benchmarks_es_op,es)
		elif menu_remover_op == '3':
			print '--------------------------------------------------'
			pais = raw_input('Pais (Case sensitive): ')
			print benchmark(es.remove,0,pais,None)
			new_menu_benchmarks_es_op = menu(menu_benchmarks_es)
			menu_menu_benchmarks_es_logic(new_menu_benchmarks_es_op,es)
		elif menu_remover_op == '4':
			print '--------------------------------------------------'
			sigla = raw_input('Sigla (Case sensitive - All Caps): ')
			print benchmark(es.remove,1,sigla,None)
			new_menu_benchmarks_es_op = menu(menu_benchmarks_es)
			menu_menu_benchmarks_es_logic(new_menu_benchmarks_es_op,es)
	elif menu_benchmarks_es_op == '3':
		print '--------------------------------------------------'
		pais = raw_input('Pais (Case sensitive): ')
		sigla = raw_input('Sigla (Case sensitive - All caps): ')
		ano_str = raw_input('Ano: ')
		try:
			ano = int(ano_str)
		except ValueError:
			print 'Opcao Invalida'
			new_menu_benchmarks_es_op = menu(menu_benchmarks_es)
			menu_menu_benchmarks_es_logic(new_menu_benchmarks_es_op,es)
			return
		perc_str = raw_input('Percentagem: ')
		try:
			perc = int(ano_str)
		except ValueError:
			print 'Opcao Invalida'
			new_menu_benchmarks_es_op = menu(menu_benchmarks_es)
			menu_menu_benchmarks_es_logic(new_menu_benchmarks_es_op,es)
			return
		print benchmark(es.insert,pais,sigla,ano,perc)
		new_menu_benchmarks_es_op = menu(menu_benchmarks_es)
		menu_menu_benchmarks_es_logic(new_menu_benchmarks_es_op,es)

def main():
	menu_logic()
	return

	#Tratar dados do ficheito dados.csv
	tratamento_de_dados(es)

	#es.paisesTree.listPaises()

	#Procurar ano nao existente
	#Por sigla
	print benchmark(es.search,1, 'PRT', 1950)
	#Por pais
	print benchmark(es.search,0, 'Portugal', 1950)

	#Procurar ano existente
	#Por sigla
	print benchmark(es.search,1, 'PRT', 1990)
	#Por pais
	print benchmark(es.search,0, 'Portugal', 1990)

	#Editar pais nao existente
	print benchmark(es.edit,1,'XP',1990,10)
	print benchmark(es.edit,0,'Xponent',1990,10)

	#Editar pais existente e data inexistente
	print benchmark(es.edit,1,'PRT',1100,10)
	print benchmark(es.edit,0,'Portugal',1100,10)

	#Editar pais existente e data existente
	print benchmark(es.edit,1,'PRT',1990,20)
	print benchmark(es.search,1, 'PRT', 1990)
	print benchmark(es.search,0, 'Portugal', 1990)
	print benchmark(es.edit,0,'Portugal',1990,50)
	print benchmark(es.search,1, 'PRT', 1990)
	print benchmark(es.search,0, 'Portugal', 1990)

	#Remover pais nao existente
	print benchmark(es.remove,1,'XP',1990)
	print benchmark(es.remove,0,'Xponent',1990)

	#Remover pais existente e data inexistente
	print benchmark(es.remove,1,'PRT',1000)
	print benchmark(es.remove,0,'Portugal',1000)

	#Remover pais existente e data existente
	print benchmark(es.remove,1,'PRT',1990)
	print benchmark(es.search,1, 'PRT', 1990)
	print benchmark(es.search,0, 'Portugal', 1990)
	print benchmark(es.remove,0,'Portugal',1990)
	print benchmark(es.search,1, 'PRT', 1990)
	print benchmark(es.search,0, 'Portugal', 1990)

	#listar anos de um pais
	#pais existente
	#beautifyListPrint(es.search(0, 'Germany', None), 'Germany')
	print benchmark(es.search,0, 'Germany', None)
	#beautifyListPrint(es.search(1, 'PRT', None), 'PRT')
	print benchmark(es.search,1, 'PRT', None)

	#pais inexistente, ano existente
	#beautifyListPrint(es.search(0, 'Xponent', None), 'Xponent')
	print benchmark(es.search,0, 'Xponent', None)
	#beautifyListPrint(es.search(1, 'XP', None), 'XP')
	print benchmark(es.search,1, 'XP', None)

	#listar paises de um ano
	#ano existente
	#beautifyListPrint(es.search(None, None, 1990), '1990')
	print benchmark(es.search,None, None, 1990)
	#ano inexistente
	#beautifyListPrint(es.search(None, None, 1000), '1000')
	print benchmark(es.search,None, None, 1000)

	#remover pais
	#pais existente
	print benchmark(es.remove,0, 'Portugal', None)
	print benchmark(es.search,0, 'Portugal', None)
	print benchmark(es.search,1, 'PRT', None)
	#pais inexistente
	print benchmark(es.remove,0, 'Xponent', None)
	print benchmark(es.search,0, 'Xponent', None)
	print benchmark(es.search,1, 'XP', None)

	#remover ano
	#ano existente
	print benchmark(es.remove,None, None, 1990)
	#beautifyListPrint(es.search(None, None, 1990), '1990')
	print benchmark(es.search,None, None, 1990)
	#ano inexistente
	print benchmark(es.remove,None, None, 1100)
	#beautifyListPrint(es.search(None, None, 1100), '1100')
	print benchmark(es.search,None, None, 1100)

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

def main1():
	es = Avl()

	es.insert('Portugal','PRT',1990,100)

if __name__ == "__main__":
	main()
