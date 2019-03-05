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
    for i in range(10):
        thisdata = data['iter0p%i'%i]
        scores.append(thisdata[0])
        xs.append(thisdata[1])
        ys.append(thisdata[2])
        cs.append(tab10(i))
    plot_once(0)
    plot_once(1,dots=(xs,ys,cs))
    pic=2
    bestx = copy.copy(xs)
    besty = copy.copy(ys)
    
    for it in range(1,40):
        
        for i in range(10):
            thisdata = data['iter%ip%i' % (it,i)]
            xs[i] = thisdata[1]
            ys[i] = thisdata[2]
            if thisdata[0] < scores[i]:
                bestx[i] = thisdata[1]
                besty[i] = thisdata[2]
                scores[i] = thisdata[0]
        plot_once(pic,dots=(xs,ys,cs), triangles=(bestx,besty,cs))
        pic+=1
    

def plot_once(i,dots=None,triangles=None,dtriangles=None):
    plt.figure()
    
    xs, ys = np.meshgrid(np.linspace(0,500,5000), np.linspace(0,500,500))
    zs = schw(xs, ys)
    plt.contourf(xs, ys, zs,levels=np.linspace(0,2000,100),cmap='Greys_r')
    if dots:
        plt.scatter(dots[0],dots[1],c=dots[2],marker='o')
    if triangles:
        plt.scatter(triangles[0],triangles[1],c=triangles[2],marker='^',s=15,edgecolors='#333333')
    if dtriangles:
        plt.scatter(dtriangles[0],dtriangles[1],c=dtriangles[2],marker='v')
    plt.axis('square')
    plt.axis([0,500,0,500])
    # plt.show()
    plt.savefig('ps%i' % i)
    

def schw(x,y):
    return  837.9658 - x * sin(sqrt(np.abs(x))) - y * sin(sqrt(np.abs(y)))
