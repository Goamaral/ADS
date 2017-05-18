from Graph import Graph
import timeit
import numpy
import matplotlib.pyplot as plt
import math

def main(nTask,nCities,start):
    G = Graph(nCities,start)
    successful = G.read(nTask)
    if (not successful):
        G.generateMap(1)
        #G.write(nTask)
    #else:
        #G.read(nTask)
    start = timeit.default_timer()
    print(G.shortestRoute('antColony').walked)
    end = timeit.default_timer()
    print(end-start)
    start = timeit.default_timer()
    print(G.shortestRoute('bruteForce')[2])
    end = timeit.default_timer()
    print(end-start)
    #G.render()

def plotAlgorithm(max,step):
    resX = []
    resY = []
    i=2
    while i <= max:
        times = []
        print(math.factorial(i))
        for j in range(10):
            start = timeit.default_timer()
            G = Graph(i,0)
            G.generateMap(1)
            G.shortestRoute('bruteForce')
            end = timeit.default_timer()
            times.append(end-start)

        print(sum(times)/len(times), i)
        resX.append(i)
        resY.append(sum(times)/len(times))
        i+=step

    coef = numpy.polynomial.polynomial.polyfit(resX, resY, 10)
    x_new = numpy.linspace(resX[0], resX[-1], num=len(resX)*10)

    ffit = numpy.polynomial.polynomial.Polynomial(coef)    # instead of np.poly1d
    plt.plot(x_new, ffit(x_new))
    #max 18
    print(poly(coef, 10))
    print(poly(coef, 11))
    plt.plot(resX, resY)
    plt.show()

def poly(coef,x):
    res = 0
    for i in range(len(coef)):
        res += coef[0] * math.pow(x,i)
    return res/10000000000

if __name__ == '__main__':
    #main(1,5,0)
    plotAlgorithm(10,1)
