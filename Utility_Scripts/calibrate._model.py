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

def polynomial(rssi, x0, x1, x2, x3, x4):
    return x0 + x1*rssi + x2*rssi**2 + x3*rssi**3 + x4*rssi**4

def calibrate():
    
    index  = list(np.argsort(avg[i]))
    sort_x = np.array((itemgetter(*index)(avg[i])), dtype = float)
    sort_y = np.array((itemgetter(*index)(dist[i])),dtype = float)
    
    
    init_vals = [1.0,1.0,1.0,1.0,1.0]
    param, _  = optimize.curve_fit(polynomial, sort_x, sort_y, p0 = init_vals)
    
    return param
   
def rsme(param):
    sum = 0
    n = len(dist[i])
    for j in range(n):
        sum = sum + ( dist[i][j] -  polynomial(avg[i][j], *param ))**2
    return np.sqrt(sum/n)

def plotModel(param):
        
    data_x = np.sort(avg[i])
    cost = rsme(param)
    plt.figure(figsize=(10.0,8.0))
    for s in range(len(dist[i])):
        plt.plot(avg[i][s],dist[i][s],'ko')
    print(cost)
    xnew = np.linspace(data_x[0], data_x[len(data_x)-1], 100)
    #print(data_x[0], data_x[len(data_x)-1])
    #plt.plot(xnew, polynomial(xnew,*param), color = "k")
    #plt.title("Polynomial Model")
    #plt.xlabel("Average of RSS (dBm)")
    #plt.ylabel("Distance (m)")
    #plt.savefig(networks[i]+"_Polymodel")
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
        param = calibrate()
        plotModel(param)
        #print(param)
        i = i + 1
        
if __name__== "__main__":
        main()