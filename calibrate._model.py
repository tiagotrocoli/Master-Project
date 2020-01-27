#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 13:33:54 2020

@author: mister-c
"""

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
def mse(x):
    sum = 0
    for j in range(22):
        sum = sum + ( avg[i][j] -  (x[0] - 10*x[1]*math.log10(dist[i][j])) )**2
    return sum/22

def calibrate():
    x0 = np.array([1.0, 1.0])
    res = minimize(mse, x0, method='BFGS', options={'xatol': 1e-8, 'disp': True})
    return res

def plotModel(x):
    
    x0 = "{0:.2f}".format(x[0])
    x1 = "{0:.2f}".format(x[1])
    
    rssi_pred = x[0] - 10*x[1]*np.log10(np.sort(dist[i]))
    
    plt.scatter(dist[i], avg[i], color = "k", marker = "o") 
    plt.plot(np.sort(dist[i]), rssi_pred, color = "k")
    
    plt.title(networks[i] + "\nrssi = " + str(x0) + " - 10*" + str(x1) + "*log(d)")
    plt.xlabel("Distance (m)")
    plt.ylabel("Average of RSSI (dBm)")
    plt.savefig(networks[i]+"_model")
    plt.show()
    
def main():
    
    global i
    m = len(networks)
    path = 'Data/'
    
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
            total = 0
            for j in range(1,11):
                num = float(lines[2+11*i+j])
                total = total + num
                rssi[i][k].append(num)
            avg[i].append(total/10.0)
            k = k + 1
        res = calibrate()
        plotModel(res.x)
        i = i + 1
        
        #plt.plot(dist[i], rssi[i], 'ko')
        #plt.title(networks[i]+" distance x rssi")
        #plt.xlabel("Distance (m)")
        #plt.ylabel("RSSI (dBm)")
        #plt.savefig(networks[i])
        
if __name__== "__main__":
        main()