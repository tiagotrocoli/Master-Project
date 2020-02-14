#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 19:56:05 2020

@author: mister-c
"""

import time
import math
import locale
import numpy as np
from openpyxl import load_workbook
from scipy.optimize import minimize

x           = [4.4, 2.2, 0, 6.6, 0, 6.6]
y           = [2.6,13.0,6.5, 10.4, 3.9, 7.8]
h           = [0.76, 1.7, 1.65, 1.17, 2.02, 1.52]
d           = [] # list of distances
l_rssi      = []
position    = []

weight = [
            [0.54,3.12,2.9,1.16,0.5,4.06],
            [1.34,2.77,2.1,14.32,1.82,1.29],
            [3.73,2.71,2.4,1.34,0.54,0.1],
            [3.88,2.54,2.68	,4.46,1.73,1.96],
            [5.16,1.38,2.46	,2.1,2.71,0.23],
            [5.38,4.06,1.57,5.11,1.17,3.33],
            [1.73,1.29,3.43	,9.78,0.62,2.54],
            [4.01,4.62,1.96	,3.29,0.68,1.33],
            [1.6,0.49,0.4,1.29,3.57,1.29],
            [0.67,1.6,1.82,2.94,0.32,0.94],
            [4.01,0.46,1.07	,4.27,0.46,1.66],
            [1.29,1.6,0.5,6.68,0.1,1.34],
            [2.77,0.94,1.6,2.27,2.27,0.84],
            [1.38,0.62,0.4,8.06,0.4,0.68],
            [0.94,0.9,4.04,5.66,0.44,4.94],
            [1.43,3.88,0.4,11.34,1.73,0.49],
            [0.77,0.18,0.62	,5.79,0.62,1.21],
            [5.82,0.93,1.07	,8.89,1.34,1.11]
            ]
total   = []
i       = 0

def mse(var):
    sum = 0
    
    for j in range(0,5):
        sum = sum + ((1.0/weight[i][j])/(total[i]))*( (x[j] - var[0])**2 + (y[j] - var[1])**2 + (h[j] - 0.73)**2 - d[j]**2)**2

    return sum

def storeData(data,sheetName):
    path    = "methods.xlsx"
    wbk     = load_workbook(path)
    page    = wbk[sheetName]
    page.append(data)
    wbk.save(path)

def findDistance(a, n, rssi):
    return 10**((a - rssi)/(10*n))

# get position and RSSI from excel
def getTestData(path):
    wbk     = load_workbook(path)
    sheet   = wbk["Average"]
    cells   = sheet['A2': 'H19']
    
    for k in range(6):
        l_rssi.append([])
    
    i = -1
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    for pos1, pos2, c1, c2, c3, c4, c5, c6 in cells:
        i = i + 1
        position.append([])
        position[i].append(locale.atof(pos1.value))
        position[i].append(locale.atof(pos2.value))
        l_rssi[0].append(locale.atof(c1.value))
        l_rssi[1].append(locale.atof(c2.value))
        l_rssi[2].append(locale.atof(c3.value))
        l_rssi[3].append(locale.atof(c4.value))
        l_rssi[4].append(locale.atof(c5.value))
        l_rssi[5].append(locale.atof(c6.value))


def circularAlgorithm(rssi):
    
    d.append(findDistance(-45.3552, 1.3843, rssi[0]) )
    d.append(findDistance(-34.2081, 1.9272, rssi[1]))
    d.append(findDistance(-33.6740, 2.2884, rssi[2]))
    d.append(findDistance(-40.0409, 2.2704, rssi[3]))
    d.append(findDistance(-35.9165, 1.9421,rssi[4]))
    #d.append(findDistance(-41.9144, 1.3344, rssi[5]))
    
    #print(rssi)
    #print(d)
    x0  = np.array([1.0, 1.0])
    res = minimize(mse, x0, method='BFGS', options={'gtol': 1e-8})
    d.clear()
    
    return [res.x[0], res.x[1]]
    

def main():
    
    getTestData('testPoints.xlsx')
    n = len(position)
    global i
    
    tol = 10**(-6)
    for k in range(n):
        soma = 0
        for p in range(5):
            soma = soma + 1.0/(weight[k][p]+tol)
        total.append(soma)
    
    while i < n:
        rssi = [l_rssi[0][i],l_rssi[1][i],l_rssi[2][i],l_rssi[3][i],l_rssi[4][i],l_rssi[5][i]]
        #calculate duration
        start = time.time()
        res = circularAlgorithm(rssi)
        duration = time.time() - start
        # calculate precision
        precision = math.sqrt( (position[i][0] - res[0])**2 + (position[i][1] - res[1])**2 )
        # put them together
        data = [position[i][0], position[i][1]]
        data.extend(res)
        data.append(duration)
        data.append(precision)
        # store in xlsx
        storeData(data,"W_CircularAlgo")
        i = i + 1
    
if __name__== "__main__":
        main()
