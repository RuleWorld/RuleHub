import matplotlib.pyplot as plt
from numpy import sin,sqrt
import numpy as np
import copy

def movie():

    data = dict()
    with open('sorted_params_final.txt') as f:
        f.readline()
        for line in f:
            parts = line.strip().split()
            data[parts[0]] = [float(x) for x in parts[1:]]
    
    tab10 = plt.cm.get_cmap('tab10')
    xs = []
    ys = []
    cs = []
    scores = []
    for i in range(5):
        thisdata = data['init%i'%i]
        scores.append(thisdata[0])
        xs.append(thisdata[1])
        ys.append(thisdata[2])
        cs.append(tab10(i))
    plot_once(0)
    plot_once(1,dots=(xs,ys,cs))
    i=2
    
    for it in range(1,20):
        oldxs = copy.copy(xs)
        oldys = copy.copy(ys)
        propx = []
        propy = []
        propcp = []
        propch = [] 
        for p in range(5):
            for h in range(5):
                if p==h:
                    continue
                thisdata = data['iter%ip%ih%i' % (it,p,h)]
                propx.append(thisdata[1])
                propy.append(thisdata[2])
                propcp.append(tab10(p))
                propch.append(tab10(h))
                if thisdata[0] < scores[p]:
                    xs[p] = thisdata[1]
                    ys[p] = thisdata[2]
                    scores[p] = thisdata[0]
        plot_once(i,dots=(oldxs,oldys,cs), triangles=(propx,propy,propcp),dtriangles=(propx,propy,propch))
        plot_once(i+1,dots=(xs,ys,cs))
        i+=2
    

def plot_once(i,dots=None,triangles=None,dtriangles=None):
    plt.figure()
    
    xs, ys = np.meshgrid(np.linspace(0,500,5000), np.linspace(0,500,500))
    zs = schw(xs, ys)
    plt.contourf(xs, ys, zs,levels=np.linspace(0,2000,100),cmap='Greys_r')
    if dots:
        plt.scatter(dots[0],dots[1],c=dots[2],marker='o')
    if dtriangles:
        plt.scatter(dtriangles[0],dtriangles[1],c=dtriangles[2],marker='v')
    if triangles:
        plt.scatter(triangles[0],triangles[1],c=triangles[2],marker='^')
    plt.axis('square')
    plt.axis([0,500,0,500])
    # plt.show()
    plt.savefig('ss%i' % i)
    

def schw(x,y):
    return  837.9658 - x * sin(sqrt(np.abs(x))) - y * sin(sqrt(np.abs(y)))
