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
from scipy import optimize
from operator import itemgetter 

i = 0
rssi = []
dist = []
avg  = []
networks = ['TiagoLocalizacao1','TiagoLocalizacao2','TiagoLocalizacao0','TiagoLocalizacao3', 'TiagoLocalizacao4',"LSC_HoneyPot"]

# mean squared errors
# x[0] = A, x[1] = n (path-loss coefficient)
# for each sensor, calibrate...

def polynomial(distance, x0, x1, x2, x3, x4):
    return x0 + x1*distance + x2*distance**2 + x3*distance**3 + x4*distance**4

def estimateDistance(rssi, limits):
    if rssi <= limits[0]:
        return polynomial(rssi,7.91684950e+05, 5.09508294e+04, 1.22886134e+03, 1.31638431e+01, 5.28442428e-02)
    elif rssi <= limits[1]:
        return polynomial(rssi,-4.04427956e+06, -2.85550202e+05, -7.55853015e+03, -8.88982335e+01, -3.91980109e-01)
    elif rssi <= limits[2]:
        return polynomial(rssi,1.55619602e+06, 1.19861197e+05, 3.46015935e+03, 4.43714107e+01, 2.13262950e-01)
    elif rssi <= limits[3]:
        return polynomial(rssi,-2.04412197e+05, -1.78192802e+04, -5.81752369e+02, -8.42988909e+00, -4.57439907e-02)

def segmentation():
    
    global sort_x, sort_y
    
    index  = list(np.argsort(avg[i]))
    sort_x = np.array((itemgetter(*index)(avg[i])), dtype = float)
    sort_y = np.array((itemgetter(*index)(dist[i])),dtype = float)
    
    n = len(index)    
    init_vals = [1.0,1.0,1.0,1.0, 1.0]
    param1, _  = optimize.curve_fit(polynomial, sort_x[0:11], sort_y[0:11], p0 = init_vals)
    param2, _  = optimize.curve_fit(polynomial, sort_x[10:21], sort_y[10:21], p0 = init_vals)
    param3, _  = optimize.curve_fit(polynomial, sort_x[20:30], sort_y[20:30], p0 = init_vals)
    param4, _  = optimize.curve_fit(polynomial, sort_x[31:n], sort_y[31:n], p0 = init_vals)
    
    
    print(param1)
    print(param2)
    print(param3)
    print(param4)
    print(round(sort_x[11],2), round(sort_x[21],2), round(sort_x[31],2), round(sort_x[n-1],2))
    
    rss = [-54.9,-37.3,-58.8,-47.9,-55.6,-45.4,-51.8,-55.7,-63.4,-55.0,-56.7,-54.8,-60.9,-56.4,-47.5,-62.9,-61.9,-60.6]
    
    for v in rss:
        print(estimateDistance(v,[-58.6, -53.0, -47.8, -43.5]))
    
    for s in range(n):
        plt.plot([rssi[i][s]],dist[i][s],'ko')
        
    xd = np.linspace(sort_x[11], sort_x[0], 100)    
    plt.plot(xd, polynomial(xd,*param1))
    xd = np.linspace(sort_x[21], sort_x[10], 100)
    plt.plot(xd, polynomial(xd,*param2))
    xd = np.linspace(sort_x[31], sort_x[20], 100)
    plt.plot(xd, polynomial(xd,*param3))
    xd = np.linspace(sort_x[n-1], sort_x[30], 100)
    plt.plot(xd, polynomial(xd,*param4))
    plt.ylim(0,12)
    plt.show()
    
def rsme(x):
    sum = 0
    div = 0
    n = len(dist[i])
    for j in range(n):
        m = len(rssi[i][j])
        div = div + m
        for k in range(m):
            sum = sum + ( dist[i][j] -  polynomial([x[0],x[1],x[2],x[3]], rssi[i][j][k]) )**2
    return np.sqrt(sum/div)

def plotModel(x, result):
    
    x0 = "{0:.4f}".format(x[0])
    x1 = "{0:.4f}".format(x[1])
    
    dd = np.sort(avg[i])
    #rssi_pred = x[0] - 10*x[1]*np.log10(np.sort(dist[i]))
    rssi_pred = polynomial(x,dd)
    #x[0] + x[1]*dd + x[2]*dd**2 + x[3]*dd**3 + x[4]*dd**4 + x[5]*dd**5
    cost = rsme(x)
    print(cost)
    plt.figure(figsize=(16.0,12.0))
    for s in range(len(dist[i])):
        plt.plot(avg[i][s],dist[i][s],'ko') 
    plt.plot(np.sort(avg[i]), rssi_pred, color = "k")
    plt.title(networks[i] + "\nrssi = " + str(x0) + " - 10*" + str(x1) + "*log(d), RSME = " + str(cost) + "\nCalibration using average rssi.")
    plt.xlabel("Distance (m)")
    plt.ylabel("Average of RSSI (dBm)")
    plt.savefig(networks[i]+"_model")
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
        #res = calibrate()
        segmentation()
        break
        #plotModel(res.x, res.fun)
        i = i + 1
        
if __name__== "__main__":
        main()