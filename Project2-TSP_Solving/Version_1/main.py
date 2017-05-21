from Graph import Graph
import time

def main(algo,nTask,nCities,start):
    G = Graph(nCities,start)
    successful = G.read(nTask)
    if (not successful):
        G.generateMap(1)
        G.write(nTask)
    else:
        G.read(nTask)
    start = time.time()
    print(G.shortestRoute(algo))
    end = time.time()
    print(end-start)

if __name__ == '__main__':
    main('dolly',1,5,0)
