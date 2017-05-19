from Graph import Graph
import time

def main(algo,nTask,nCities,start):
    G = Graph(nCities,start)
    successful = G.read(nTask)
    if (not successful):
        G.generateMap(nTask)
        G.write(nTask)
    else:
        G.read(nTask)
    start = time.time()
    print(G.shortestRoute(algo))
    end = time.time()
    print(end-start)
    print(end-start)
    #G.render()

if __name__ == '__main__':
    main('bruteForce',1,10,0)
