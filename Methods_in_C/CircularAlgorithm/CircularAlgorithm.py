#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 13:27:22 2020

@author: mister-c
"""

import time
import math
import numpy as np
from openpyxl import load_workbook
from scipy.optimize import minimize

x           = [4.4, 2.2, 0, 6.6, 0, 6.6]
y           = [2.6,13.0,6.5, 10.4, 3.9, 7.8]
h           = [0.76, 1.7, 1.65, 1.17, 2.02, 1.52]
d           = [] # list of distances

def mse(var):
    sum = 0
    
    for i in range(6):
        sum = sum + ( (x[i] - var[0])**2 + (y[i] - var[1])**2 + (h[i] - 0.73)**2 - d[i]**2)**2

    return sum

def storePosition(data,sheetName):
    path    = "methods.xlsx"
    wbk     = load_workbook(path)
    page    = wbk[sheetName]
    page.append(data)
    wbk.save(path)


def circularAlgorithm():
    
    # get RSSI from excel
    
    d.append(5.10890399205)
    d.append(6.66340003302)
    d.append(1.43401534162)
    d.append(6.75674477837)
    d.append(3.10388466281)
    d.append(5.70649629808)
        
    x0  = np.array([1.0, 1.0])
    res = minimize(mse, x0, method='BFGS', options={'gtol': 1e-8})
    
    return [res.x[0], res.x[1]]
    

# get RSSI from excel
position = [1.1,6.5]
#calculate duration
start = time.time()
res = circularAlgorithm()
duration = time.time() - start
# calculate precision
precision = math.sqrt( (position[0] - res[0])**2 + (position[1] - res[1])**2 )
# put them together
position.extend(res)
position.append(duration)
position.append(precision)
# store in xlsx
storePosition(position,"CircularAlgo")