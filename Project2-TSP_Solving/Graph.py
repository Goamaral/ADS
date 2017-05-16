import networkx as nx
import matplotlib.pyplot as plt
import sys
import random
import itertools
from Dolly import Dolly
from Population import Population

class Graph:
    def __init__(self, nCities, start):
        self.g = nx.DiGraph()
        self.start = start
        self.nCities = nCities
        self.g.add_nodes_from([str(x) for x in range(nCities)])

    def render(self):
        new_labels = dict(map(lambda x:((x[0],x[1]), str(x[2]['weight'])), self.g.edges(data = True)))
        pos = nx.spring_layout(self.g)
        nx.draw_networkx(self.g, pos=pos)
        nx.draw_networkx_edge_labels(self.g, pos=pos, edge_labels = new_labels)
        nx.draw_networkx_edges(self.g, pos)
        plt.show()

    def generateMap(self,nWay):
        if nWay == 1:
            for i in range(self.nCities):
                for j in range(i+1, self.nCities):
                    w = random.randint(1,50)
                    self.connect([str(i),str(j),str(w)])
        elif nWay == 2:
            for i in range(self.nCities):
                for j in range(i+1, self.nCities):
                    w1 = random.randint(1,50)
                    w2 = random.randint(1,50)
                    self.connect([str(i),str(j),str(w1),str(w2)])
        else:
            raise TypeError

    def connect(self, arr):
        if len(arr) == 3:
            self.g.add_weighted_edges_from([(arr[0],arr[1],arr[2]), (arr[1],arr[0],arr[2])])
        elif len(arr) == 4:
            self.g.add_weighted_edges_from([(arr[0],arr[1],arr[2]), (arr[1],arr[0],arr[3])])
        else:
            raise TypeError

    def write(self,nTask):
        nx.write_edgelist(self.g,path="tarefa_{}_{}.txt".format(nTask, self.nCities),delimiter=" - ")
        print('Data outputed')

    def read(self,nTask):
        try:
            H = nx.read_edgelist(path="tarefa_{}_{}.txt".format(nTask, self.nCities),delimiter=" - ")
        except FileNotFoundError:
            return False
        self.g = nx.DiGraph(H)
        return True
        print('Data read')

    def shortestRoute(self,algo):
        if algo == 'antColony':
            return self.antColony()
        elif algo == 'bruteForce':
            return self.bruteForce()

    def bruteForce(self):
        routes = []
        distanceTotal = []
        distances = []
        nodes = self.g.nodes()
        nodes.remove(str(self.start))

        routes = list(itertools.permutations(nodes, len(nodes)))

        for route in routes:
            aux = self.calcDistance(list(route))
            distances.append(aux)
            distanceTotal.append(sum(aux))

        return ['0']+list(routes[distances.index(min(distances))])+['0'], distances, min(distanceTotal)

    def antColony(self):
        marksLeft = self.g.nodes()
        marksLeft.remove(str(self.start))
        population = Population(self.g,[Dolly(self.g,[str(self.start)],marksLeft)])

        while True:
            successful,result = population.update()
            if successful:
                break
        return result

    def calcDistance(self,route):
        res = [int(self.g.edge[str(self.start)][route[0]]['weight'])]
        for i in range(len(route)-1):
            res.append(int(self.g.edge[route[i]][route[i+1]]['weight']))
        res.append(int(self.g.edge[route[-1]][str(self.start)]['weight']))
        return res
