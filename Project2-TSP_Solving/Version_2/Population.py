class Population:
    def __init__(self,labirinth,sheep):
        self.labirinth = labirinth
        self.ready = []
        self.walking = []
        self.ready = [sheep]

    def update(self):
        sheep = []
        for s in self.ready:
            if len(s.marks) > 1 and s.marks[-1] == s.marks[0]:
                return True, s
            sheep = s.clone(sheep)

        self.ready = []
        self.walking.extend(sheep)

        if self.walking:
            mn = min(self.walking, key=lambda s: s.toWalk).toWalk
            repeat = True
            i=0
            remove = False
            while repeat:
                size = len(self.walking)
                while i < size:
                    s = self.walking[i]
                    s.walked = s.walked + mn
                    if s.toWalk == mn:
                        s.toWalk = 0
                        s.marks.append(s.towards)
                        if len(s.marks) > 1 and s.marks[-1] == s.marks[0]:
                            return True, s
                        s.marksLeft.remove(s.towards)
                        s.towards = None
                        self.ready.append(s)
                        remove = True
                        break
                    else:
                        s.toWalk = s.toWalk - mn
                    i+=1
                if remove:
                    self.walking.remove(s)
                    remove = False
                if i==size:
                    repeat = False

        return False, self
