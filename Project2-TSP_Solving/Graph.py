import networkx as nx
import matplotlib.pyplot as plt
import sys
import random

class Graph:
    def __init__(self, nCities, start):
        self.g = nx.DiGraph()
        self.start = start
        self.nCities = nCities
        self.g.add_nodes_from([x for x in range(nCities)])

    def render(self):
        new_labels = dict(map(lambda x:((x[0],x[1]), str(x[2]['weight'])), self.g.edges(data = True)))
        pos = nx.spring_layout(self.g)
        nx.draw_networkx(self.g, pos=pos)
        nx.draw_networkx_edge_labels(self.g, pos=pos, edge_labels = new_labels)
        nx.draw_networkx_edges(self.g, pos)
        plt.show()

    def generateMapOneWayWeight(self):
        for i in range(self.nCities):
            for j in range(i+1, self.nCities):
                w = int(random.random()*10+1)
                self.connect([i,j,w])

    def connect(self, arr):
        if len(arr) == 3:
            self.g.add_weighted_edges_from([(arr[0],arr[1],arr[2]), (arr[1],arr[0],arr[2])])
        elif len(arr) == 4:
            self.g.add_weighted_edges_from([(arr[0],arr[1],arr[2]), (arr[1],arr[0],arr[3])])
        else:
            raise TypeError

    def write(self,nTask):
        nx.write_edgelist(self.g,path="tarefa_{}_{}.txt".format(nTask, self.nCities),delimiter=" - ")

    def read(self,nTask):
        try:
            H = nx.read_edgelist(path="tarefa_{}_{}.txt".format(nTask, self.nCities),delimiter=" - ")
        except FileNotFoundError:
            return False
        self.g = nx.DiGraph(H)
        return True
