#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 16:35:28 2020

@author: mister-c
"""

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 13:33:54 2020

@author: mister-c
"""

# Calibration using the average points of RSSI.

import os
import math
from scipy.optimize import minimize
import numpy as np
import matplotlib.pyplot as plt

i = 0
rssi = []
dist = []
avg  = []
networks = ['TiagoLocalizacao1','TiagoLocalizacao2','TiagoLocalizacao0','TiagoLocalizacao3', 'TiagoLocalizacao4',"LSC_HoneyPot"]

# mean squared errors
# x[0] = A, x[1] = n (path-loss coefficient)
# for each sensor, calibrate...
def mse(x):
    
    total = 0
    n = len(dist[i])
    for j in range(n):
        total = total + ( avg[i][j] -  (x[0] - 10*x[1]*math.log10(dist[i][j])) )**2
    return total/n

def mse1(x):
    
    total = 0
    n = len(dist[i])
    for j in range(n):
        total = total + (dist[i][j] - findDistance(x[0], x[1], avg[i][j]))**2
    return total/n

def calibrate():
    x0 = np.array([1.0, 1.0])
    res = minimize(mse1, x0, method='BFGS', options={'gtol': 1e-8, 'disp': True})
    return res

def findDistance(a, n, rss):
    return 10**((a - rss)/(10*n))

def plotModel(x, fun):
    
    cost = np.sqrt(fun)
    print(round(x[0],4),round(x[1],4))
    
    plt.figure(figsize=(16.0,12.0))
    for s in range(len(dist[i])):
        plt.plot(avg[i][s], dist[i][s],'ko')
        
    data_x = np.sort(avg[i])
    xnew = np.linspace(data_x[0], data_x[len(data_x)-1], 100)
    
    result = []
    for l in range(100):
        result.append(findDistance(x[0],x[1],xnew[l]))
    
    plt.plot(xnew, result, color = "k")
    plt.title("Lognormal Path-loss Model", fontsize = 18)
    plt.xlabel("Average of RSS (dBm)", fontsize = 18)
    plt.ylabel("Distance (m)", fontsize = 18)
    #plt.savefig(networks[i]+"_lognormal")
    plt.ylim(0,12)
    #plt.show()
    
def removeDuplicate(dist,rssi):
    
    for i in range(len(dist)):
        j = i + 1
        while(j < len(dist)):
            if dist[i] == dist[j]:
                rssi[i].extend(rssi[j])
                rssi.pop(j)
                dist.pop(j)
            else:
                j = j + 1
    
    return (dist, rssi)
    
def main():
    
    global i
    m = len(networks)
    path = '../Data/RSSI/'
    
    while(i < m):
        dist.append([])
        rssi.append([])
        avg.append([])
        k = 0
        for filename in os.listdir(path):
            file  = open(path+filename, "r")
            lines = file.readlines()
            dist[i].append(float(lines[2+11*i].split(" ")[1]))
            rssi[i].append([])
            for j in range(1,11):
                rssi[i][k].append(float(lines[2+11*i+j]))
            k = k + 1
            
        dist[i], rssi[i] = removeDuplicate(dist[i], rssi[i])
        for s in range(len(dist[i])):
            avg[i].append( np.sum(rssi[i][s])/(1.0*len(rssi[i][s])) )
        res = calibrate()
        plotModel(res.x, res.fun)
        i = i + 1
        
if __name__== "__main__":
        main()
