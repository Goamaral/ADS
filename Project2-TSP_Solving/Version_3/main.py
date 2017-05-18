from Graph import Graph
import time
import numpy
import matplotlib.pyplot as plt
import math

def main(nTask,nCities,start):
    G = Graph(nCities,start)
    successful = G.read(nTask)
    if (not successful):
        G.generateMap(nTask)
        G.write(nTask)
    else:
        G.read(nTask)
    start = time.time()
    print(G.shortestRoute('dolly').walked)
    end = time.time()
    print(end-start)
    start = time.time()
    print(G.shortestRoute('bruteForce')[2])
    end = time.time()
    print(end-start)
    #G.render()

def plotAlgorithm(algo,nTask):
    resX = []
    resY = []
    i=2
    while i <= 11:
        times = []
        print(math.factorial(i))
        for j in range(20):
            G = Graph(i,0)
            G.generateMap(1)
            G.write(nTask)
            start = time.time()
            G.shortestRoute(algo)
            end = time.time()
            times.append(end-start)
            print(i,j,end-start)

        print(sum(times)/len(times), i)
        resX.append(i)
        resY.append(sum(times)/len(times))
        i+=1

    coef = numpy.polynomial.polynomial.polyfit(resX, resY, 10)
    x_new = numpy.linspace(resX[0], resX[-1], num=len(resX)*10)

    ffit = numpy.polynomial.polynomial.Polynomial(coef)    # instead of np.poly1d
    plt.plot(x_new, ffit(x_new))
    #max 18
    print(poly(coef, 10))
    print('30min = 1800sec')
    print(14, poly(coef, 14))
    print(15, poly(coef, 15))
    plt.plot(resX, resY)
    plt.show()

def poly(coef,x):
    res = 0
    for i in range(len(coef)):
        res += coef[i] * math.pow(x,i)
    return res

if __name__ == '__main__':
    main(2,11,0)
    #plotAlgorithm('dolly',1)
