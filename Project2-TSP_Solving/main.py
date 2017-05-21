from Version_1 import Graph as Graph_v1
from Version_2 import Graph as Graph_v2
import time

def printTitle(title):
    print('----------')
    print(title)
    print('----------')

def menu(lmenu):
    for l in lmenu:
        i = lmenu.index(l)
        if i == 0:
            printTitle(l)
        else:
            print('{}: {}'.format(i,l))
    print()
    return numberInput('Opcao: ')

def numberInput(label,interval=None):
    try:
        a = int(input(label))
    except ValueError:
        printTitle('Valor Invalido')
        return numberInput(label)
    if interval == None:
        return a
    elif a >= interval[0] and (interval[1] == 'inf' or a < interval[1]):
            return a
    else:
        printTitle('Valor Invalido - Nao se encontra no intervalo de numeros validos\n{} <= input < {}'.format(interval[0], interval[1]))
        return numberInput(label,interval)

def BinaryInput(label, accept):
    a = input(label)
    return a in accept

def readLine(label):
    return input(label)

def runAlgo(algo,G):
    algos = [ None, 'dolly', 'bruteForce' ]
    start = time.time()
    res = G.shortestRoute(algos[algo])
    end = time.time()
    printTitle('Resultado')
    print(res)
    print('Tempo: ', end-start)
    saveMap = BinaryInput('Guardar mapa[S/n]: ', 'Ss')
    if saveMap:
        filename = readLine('Nome do ficheiro: ')
        G.write(filename)

def main():
    menuPrincipal = [ 'Numero da tarefa', 'Tarefa 1', 'Tarefa 2', 'Sair' ]
    menuTarefa = [ 'Algoritmo', 'Dolly (Criado por nos)', 'BruteForce', 'Voltar' ]
    menuVersao = [ 'Versao', 'Versao base', 'Versao optimizada', 'Voltar' ]
    inputsStartAlgo = [ 'Dados Algoritmo', 'Numero cidades: ', 'Numero cidade de comeco: ', 'Criar mapa novo[S/n]: ' ]
    inputsEndAlgo = [ 'Guardar mapa[S/n]: ' ]

    while True:
        task = menu(menuPrincipal)
        if task in [1,2]:
            while True:
                algo = menu(menuTarefa)
                if algo in [1,2]:
                    while True:
                        version = menu(menuVersao)
                        if version in [1,2]:
                            if version == 1:
                                G = Graph_v1.Graph(2,0)
                            else:
                                G = Graph_v2.Graph(2,0)
                            readMap = BinaryInput(inputsStartAlgo[3], 'Ss')
                            if readMap:
                                printTitle(inputsStartAlgo[0])
                                nCities = numberInput(inputsStartAlgo[1], (2,'inf'))
                                start = numberInput(inputsStartAlgo[2], (0,nCities))
                                if version == 1:
                                    G = Graph_v1.Graph(nCities,start)
                                else:
                                    G = Graph_v2.Graph(nCities,start)
                                G.generateMap(task)
                            else:
                                mapRead = False
                                while not mapRead:
                                    filename = readLine('Nome do ficheiro: ')
                                    if filename == '':
                                        G.generateMap(task)
                                        break
                                    mapRead = G.read(filename)
                                start = numberInput(inputsStartAlgo[2], (0,len(G.g.nodes())))
                                G.start = start
                            runAlgo(algo,G)
                            break
                        elif version == 3:
                            break
                        else:
                            printTitle('Opcao Invalida')
                elif algo == 3:
                    break
                else:
                    printTitle('Opcao Invalida')
        elif task == 3:
            break
        else:
            printTitle('Opcao Invalida')


if __name__ == '__main__':
    main()
