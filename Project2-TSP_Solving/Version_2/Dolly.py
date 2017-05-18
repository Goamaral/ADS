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
        s = '{} {} {} {} {}'.format(self.marks,self.marksLeft,self.walked,self.toWalk,self.towards)
        return s

    def copy(self,toWalk,towards):
        clone = Dolly(self.labirinth,[ i for i in self.marks ],[ i for i in self.marksLeft ])
        clone.walked = self.walked
        clone.toWalk = toWalk
        clone.towards = towards
        return clone

    def clone(self,group):
        cloned = False
        roads = self.labirinth[str(self.marks[-1])]
        for road in roads:
            intRoad = int(road)
            if intRoad in self.marksLeft:
                clone = self.copy(int(roads[road]['weight']),intRoad)
                group.append(clone)
                cloned = True
        if not cloned:
            clone = self.copy(int(roads[str(self.marks[0])]['weight']),self.marks[0])
            group.append(clone)
        return group
