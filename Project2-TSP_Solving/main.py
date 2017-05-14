from Graph import Graph

def main(nTask,nCities,start):
    G = Graph(nCities,start)
    successful = G.read(nTask)
    if (not successful):
        G.generateMapOneWayWeight()
        G.write(nTask)
    else:
        G.read(nTask,nCities)
    G.render()

if __name__ == '__main__':
    main(1,4,0)
