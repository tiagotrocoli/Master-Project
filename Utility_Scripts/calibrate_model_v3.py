#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 16:31:25 2020

@author: tiago
"""

import os
import math
from scipy.optimize import minimize
import numpy as np
import matplotlib.pyplot as plt
from openpyxl import load_workbook
import matplotlib


path = "../Data/"

i = 0
n = 37
dist = []
avg  = []
networks = ['TiagoLocalizacao1','TiagoLocalizacao2','TiagoLocalizacao0','TiagoLocalizacao10', 'TiagoLocalizacao11',"TiagoLocalizacao12"]

# mean squared errors
# x[0] = A, x[1] = n (path-loss coefficient)
# for each sensor, calibrate...

def mse1(x):
    
    total = 0
    for j in range(n):
        total = total + (dist[j][i] - findDistance(x[0], x[1], avg[j][i]))**2
    return total/n

def calibrate():
    x0 = np.array([1.0, 1.0])
    res = minimize(mse1, x0, method='L-BFGS-B', options={'gtol': 1e-8, 'disp': False})
    return res

def findDistance(a, n, rss):
    return 10**((a - rss)/(10*n))

def plotModel(x, fun):
    
    cost = np.sqrt(fun)
    
    plt.figure(figsize=(10.0,8.0))
    rss = []
    for s in range(n):
        rss.append(avg[s][i])
        plt.plot(avg[s][i], dist[s][i],'ko')
    
    data_x = np.sort(rss)
    xnew = np.linspace(data_x[0], data_x[len(data_x)-1], 100)
    
    result = []
    for l in range(100):
        result.append(findDistance(x[0],x[1],xnew[l]))
        
    plt.rcParams.update({'font.size': 20})
    plt.plot(xnew, result, color = "k")
    plt.title("Lognormal Path-loss Model (Experiment 2)")
    plt.xlabel("Average of RSS (dBm)")
    plt.ylabel("Distance (m)")
    plt.savefig(networks[i]+"_lognormal_2")
    plt.show()
    
def getData2(ini, end):
    doc    = "dataBase.xlsx"
    wbk     = load_workbook(path+doc)
    sheet   = wbk["dist_rss"]
    cells   = sheet[ini : end]
    
    #locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    for dist1, dist2, dist3, dist4, dist5, dist6, rss1, rss2, rss3, rss4, rss5, rss6 in cells:
        dist.append([dist1.value, dist2.value, dist3.value, dist4.value, dist5.value, dist6.value])
        avg.append([rss1.value, rss2.value, rss3.value, rss4.value, rss5.value, rss6.value])
    
def main():
    
    global i
    m = len(networks)
    getData2("A2", "L38")
    
    while(i < m):
        res = calibrate()
        plotModel(res.x, res.fun)
        i = i + 1
        
if __name__== "__main__":
        main()