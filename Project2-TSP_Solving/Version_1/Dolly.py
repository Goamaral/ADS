import copy

class Dolly:
    def __init__(self,labirinth,marks,marksLeft):
        self.labirinth = labirinth
        self.marks = marks
        self.marksLeft = marksLeft
        self.walked = 0
        self.toWalk = 0
        self.towards = None

    def __str__(self):
        s = 'Rota: {}\nDistancia: {}'.format(self.marks,self.walked)
        return s

    def clone(self):
        clones = []
        roads = self.labirinth[self.marks[-1]]
        for road in roads:
            if road in self.marksLeft:
                clone = copy.deepcopy(self)
                clone.toWalk = roads[road]['weight']
                clone.towards = road
                clones.append(clone)
        if len(clones) == 0:
            clone = copy.deepcopy(self)
            clone.toWalk = roads[self.marks[0]]['weight']
            clone.towards = self.marks[0]
            clones.append(clone)
        return clones
