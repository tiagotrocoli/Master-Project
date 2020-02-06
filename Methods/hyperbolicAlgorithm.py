#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 13:45:22 2020

@author: mister-c
"""

import time
import math
import numpy as np
from numpy.linalg import inv
from openpyxl import load_workbook

x           = [4.4, 2.2, 0, 6.6, 0, 6.6]
y           = [2.6,13.0,6.5, 10.4, 3.9, 7.8]
h           = [0.76, 1.7, 1.65, 1.17, 2.02, 1.52]
d           = []


def storePosition(data,sheetName):
    path    = "methods.xlsx"
    wbk     = load_workbook(path)
    page    = wbk[sheetName]
    page.append(data)
    wbk.save(path)
    

def hyperbolicAlgorithm():
    
    d.append(5.10890399205)
    d.append(6.66340003302)
    d.append(1.43401534162)
    d.append(6.75674477837)
    d.append(3.10388466281)
    d.append(5.70649629808)
    
    A = np.matrix([[ 2*(x[5] - x[0]), 2*(y[5] - y[0]) ], 
                   [ 2*(x[5] - x[1]), 2*(y[5] - y[1]) ],
                   [ 2*(x[5] - x[2]), 2*(y[5] - y[2]) ],
                   [ 2*(x[5] - x[3]), 2*(y[5] - y[3]) ],
                   [ 2*(x[5] - x[4]), 2*(y[5] - y[4]) ]
                  ], dtype=np.float64)
    b= np.matrix([
                [d[0]**2 - d[5]**2 - x[0]**2 - y[0]**2 + x[5]**2 + y[5]**2],
                [d[1]**2 - d[5]**2 - x[1]**2 - y[1]**2 + x[5]**2 + y[5]**2],
                [d[2]**2 - d[5]**2 - x[2]**2 - y[2]**2 + x[5]**2 + y[5]**2],
                [d[3]**2 - d[5]**2 - x[3]**2 - y[3]**2 + x[5]**2 + y[5]**2],
                [d[4]**2 - d[5]**2 - x[4]**2 - y[4]**2 + x[5]**2 + y[5]**2]
                ], dtype=np.float64)
    
    AT  = A.transpose()
    AAT = AT.dot(A)
    
    try:
        var = (inv(AAT)*AT*b).tolist()
        return [var[0][0], var[1][0]]
    except:
        print("Could not solve since matrix has no inverse.")
        return -1


# get RSSI from excel
position = [1.3,6.5]
#calculate duration
start = time.time()
res = hyperbolicAlgorithm()
duration = time.time() - start
# calculate precision
precision = math.sqrt( (position[0] - res[0])**2 + (position[1] - res[1])**2 )
# put them together
position.extend(res)
position.append(duration)
position.append(precision)
# store in xlsx
storePosition(position,"HyperbolicAlgo")