#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 15:06:40 2020

@author: mister-c
"""

import os
import math
from scipy.optimize import minimize
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

i = 0
rssi = []
dist = []
avg  = []
networks = ['TiagoLocalizacao1','TiagoLocalizacao2','TiagoLocalizacao0','TiagoLocalizacao3', 'TiagoLocalizacao4',"LSC_HoneyPot"]

# mean squared errors
# x[0] = A, x[1] = n (path-loss coefficient)
# for each sensor, calibrate...

def lognormal(x, distance):
    return x[0] - 10*x[1]*math.log10(distance)

def polynomial(x,distance):
    return x[0] + x[1]*distance + x[2]*distance**2 + x[3]*distance**3 + x[4]*distance**4 + x[5]*distance**5

def mse(x):
    sum = 0
    n = len(dist[i])
    for j in range(n):
        sum = sum + ( avg[i][j] -  lognormal([x[0],x[1]], dist[i][j]) )**2
    return sum/n

def calibrate():
    x0 = np.array([1.0, 1.0, 1.0, 1.0, 1.0,1.0])
    res = minimize(mse, x0, method='BFGS', options={'gtol': 1e-8, 'disp': False})
    return res

def interpolate():
    x = []
    y = []
    for j in range(0,30,4):
        x.append(avg[i][j])
        y.append(dist[i][j])
    #x = np.array(x)
    #y = np.array(y)
    f2 = interp1d(y,x, kind='cubic', assume_sorted=False, fill_value="extrapolate")
    xnew = np.linspace(1, 10, num=50, endpoint=True)
    plt.plot(dist[i],avg[i], 'o', xnew, f2(xnew), '--')
    plt.axis((1,10,-10,-70))
    plt.show()
    
def rsme(x):
    sum = 0
    div = 0
    n = len(dist[i])
    for j in range(n):
        m = len(rssi[i][j])
        div = div + m
        for k in range(m):
            sum = sum + ( rssi[i][j][k] -  lognormal([x[0],x[1]], dist[i][j]) )**2
    return np.sqrt(sum/div)

def plotModel(x, result):
    
    x0 = "{0:.4f}".format(x[0])
    x1 = "{0:.4f}".format(x[1])
    
    rssi_pred = x[0] - 10*x[1]*np.log10(np.sort(dist[i]))
    cost = rsme(x)
    print(cost)
    plt.figure(figsize=(16.0,12.0))
    for s in range(len(dist[i])):
        plt.plot(dist[i][s],avg[i][s],'ko') 
    plt.plot(np.sort(dist[i]), rssi_pred, color = "k")
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
        res = interpolate()
        #plotModel(res.x, res.fun)
        i = i + 1
        
if __name__== "__main__":
        main()