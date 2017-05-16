import copy

class Population:
    def __init__(self,labirinth,sheep):
        self.labirinth = labirinth
        self.ready = []
        self.walking = []
        self.insert(sheep)

    def insert(self,sheep):
        for s in sheep:
            if s.toWalk == 0:
                self.ready.append(s)
            else:
                self.walking.append(s)
        if len(self.walking) > 0:
            self.walking = sorted(self.walking,key=lambda s: int(s.toWalk))

    def update(self):
        sheep = []
        while len(self.ready) > 0:
            s = self.ready[0]
            if len(s.marks) > 1 and s.marks[-1] == s.marks[0]:
                return True, s
            sheep.extend(s.clone())
            self.ready.pop(0)
        self.insert(sheep)

        if len(self.walking) > 0:
            mn = self.walking[0].toWalk
            for s in self.walking:
                s.walked = str(int(s.walked) + int(mn))
                if s.toWalk == mn:
                    s.toWalk = 0
                    s.marks.append(s.towards)
                    if len(s.marks) > 1 and s.marks[-1] == s.marks[0]:
                        return True, s
                    s.marksLeft.remove(s.towards)
                    s.towards = None
                    self.ready.append(s)
                else:
                    s.toWalk = str(int(s.toWalk) - int(mn))

            while len(self.walking) > 0 and self.walking[0].toWalk == 0:
                self.walking.pop(0)

        return False, self
