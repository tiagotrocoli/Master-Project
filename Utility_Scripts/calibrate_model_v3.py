#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 16:31:25 2020

@author: tiago
"""

import os
import math
from scipy import optimize
import numpy as np
import matplotlib.pyplot as plt
from operator import itemgetter 
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
        total = total + (dist[j][i] - polynomial(avg[j][i], x[0], x[1], x[2], x[3], x[4]))**2
    return total/n

#def calibrate():
#    x0 = np.array([1.0, 1.0, 2.0, 0.5, 3.0])
#    res = minimize(mse1, x0, method='L-BFGS-B', options={'gtol': 1e-8, 'disp': False})
#    return res

def calibrate():
    
    rss_i  = []
    dist_i = []
    for s in range(n):
        rss_i.append(avg[s][i])
        dist_i.append(dist[s][i])
        
    index  = list(np.argsort(rss_i))
    sort_x = np.array((itemgetter(*index)(rss_i)), dtype = float)
    sort_y = np.array((itemgetter(*index)(dist_i)),dtype = float)
 
    init_vals = [1.0,1.0, 0.0, 0.0, 2.0]
    param, _  = optimize.curve_fit(polynomial, sort_x, sort_y, p0 = init_vals)
    return param

def rsme(param):
    sum = 0
    n = len(dist[i])
    for j in range(n):
        sum = sum + ( dist[i][j] -  polynomial(avg[i][j], *param ))**2
    return np.sqrt(sum/n)

def lognormal(rss, a, n):
    return 10**((a - rss)/(10*n))

def polynomial(rssi, x0, x1, x2, x3, x4):
    return x0 + x1*rssi + x2*rssi**2 + x3*rssi**3 + x4*rssi**4

def plotModel(param):
        
    data_x = np.sort(avg[i])
    print(rsme(param))
    plt.figure(figsize=(10.0,8.0))
    rss = []
    for s in range(n):
        rss.append(avg[s][i])
        plt.plot(avg[s][i], dist[s][i],'ko')
    data_x = np.sort(rss)
    xnew = np.linspace(data_x[0], data_x[len(data_x)-1], 100)
    #print(*param)
    #print(data_x[0], data_x[len(data_x)-1])
    #plt.rcParams.update({'font.size': 20})
    plt.plot(xnew, polynomial(xnew,*param), color = "k")
    plt.title("Lognormal Model (2nd experiment)", fontsize = 28)
    plt.xlabel("Average of RSS (dBm)", fontsize = 28)
    plt.ylabel("Distance (m)", fontsize = 28)
    plt.savefig(networks[i]+"_Lognormal_exp2")
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
        param = calibrate()
        #print(rsme(param), param)
        plotModel(param)
        i = i + 1
        
if __name__== "__main__":
        main()
