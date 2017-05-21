import networkx as nx
import matplotlib.pyplot as plt
import numpy
import itertools
from . import Dolly as d
from . import Population as p

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
                    w = numpy.random.randint(1,100)
                    self.connect([str(i),str(j),str(w)])
        elif nWay == 2:
            for i in range(self.nCities):
                for j in range(i+1, self.nCities):
                    [w1,w2] = numpy.random.randint(1,100,size=2)
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

    def write(self,filename):
        nx.write_edgelist(self.g,path="{}.txt".format(filename),delimiter=" - ")

    def read(self,filename):
        try:
            H = nx.read_edgelist(path="{}.txt".format(filename),delimiter=" - ")
        except FileNotFoundError:
            return False
        self.g = nx.DiGraph(H)
        return True

    def shortestRoute(self,algo):
        if algo == 'dolly':
            return self.dolly()
        elif algo == 'bruteForce':
            return self.bruteForce()

    def bruteForce(self):
        routes = []
        distanceTotal = []
        distances = []
        nodes = [ int(x) for x in self.g.nodes() ]
        nodes.remove(self.start)

        routes = list(itertools.permutations(nodes, len(nodes)))

        for route in routes:
            aux = self.calcDistance(list(route))
            distances.append(aux)
            distanceTotal.append(sum(aux))

        minDist = min(distanceTotal)
        ind = distanceTotal.index(minDist)
        route = [self.start] + list(routes[ind]) + [self.start]

        return "Rota: {}\nDistancia: {}".format(route,minDist)

    def dolly(self):
        marksLeft = [ int(x) for x in self.g.nodes() ]
        marksLeft.remove(self.start)
        population = p.Population(self.g,d.Dolly(self.g,[self.start],marksLeft))

        while True:
            successful,result = population.update()
            if successful:
                return result

    def calcDistance(self,route):
        res = [int(self.g.edge[str(self.start)][str(route[0])]['weight'])]
        for i in range(len(route)-1):
            res.append(int(self.g.edge[str(route[i])][str(route[i+1])]['weight']))
        res.append(int(self.g.edge[str(route[-1])][str(self.start)]['weight']))
        return res
