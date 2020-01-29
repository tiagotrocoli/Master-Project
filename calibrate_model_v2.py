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
networks = ['TiagoLocalizacao1','TiagoLocalizacao2','TiagoLocalizacao0','TiagoLocalizacao3', 'TiagoLocalizacao4',"LSC_HoneyPot"]

# mean squared errors
# x[0] = A, x[1] = n (path-loss coefficient)
# for each sensor, calibrate...
def mse(x):
    sum = 0
    div = 0
    n = len(dist[i])
    for j in range(n):
        m = len(rssi[i][j])
        div = div + m
        for k in range(m):
            sum = sum + ( rssi[i][j][k] -  (x[0] - 10*x[1]*math.log10(dist[i][j])) )**2
    return sum/div

def calibrate():
    x0 = np.array([1.0, 1.0])
    res = minimize(mse, x0, method='BFGS', options={'xatol': 1e-8, 'disp': True})
    return res

def plotModel(x, fun):
    
    x0 = "{0:.4f}".format(x[0])
    x1 = "{0:.4f}".format(x[1])
    
    rssi_pred = x[0] - 10*x[1]*np.log10(np.sort(dist[i]))
    cost = np.sqrt(fun)
    
    plt.figure(figsize=(16.0,12.0))
    for s in range(len(dist[i])):
        plt.plot(dist[i][s],[rssi[i][s]],'ko') 
    plt.plot(np.sort(dist[i]), rssi_pred, color = "k")
    plt.title(networks[i] + "\nrssi = " + str(x0) + " - 10*" + str(x1) + "*log(d), RSME = " + str(cost) + "\nCalibration using all rssi.")
    plt.xlabel("Distance (m)")
    plt.ylabel("RSSI (dBm)")
    plt.savefig(networks[i]+"_model_all")
    plt.show()
    
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
    path = 'Data/'
    
    while(i < m):
        dist.append([])
        rssi.append([])
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
        res = calibrate()
        plotModel(res.x, res.fun)
        i = i + 1
        
if __name__== "__main__":
        main()