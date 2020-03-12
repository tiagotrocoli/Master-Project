#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 17:04:36 2020

@author: mister-c
"""

from sklearn.neural_network import MLPRegressor
from sklearn import svm
import sys
import time
import math
import numpy as np
import locale
from openpyxl import load_workbook

x           = [4.4, 2.2, 0, 6.6, 0, 6.6]
y           = [2.6,13.0,6.5, 10.4, 3.9, 7.8]
h           = [0.76, 1.7, 1.65, 1.17, 2.02, 1.52]


def storeData(data,sheetName):
    path    = "methods.xlsx"
    wbk     = load_workbook(path)
    page    = wbk[sheetName]
    page.append(data)
    wbk.save(path)

def getData(path, page, ini, end):
    wbk     = load_workbook(path)
    sheet   = wbk[page]
    cells   = sheet[ini : end]
    
    position = []
    row = []

    i = -1
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    for pos1, pos2, c1, c2, c3, c4, c5 in cells:
        i = i + 1
        position.append([])
        position[i].append(locale.atof(pos1.value))
        position[i].append(locale.atof(pos2.value))
        row.append([locale.atof(c1.value), locale.atof(c2.value), locale.atof(c3.value), locale.atof(c4.value), locale.atof(c5.value)])
    
    return row, position

def main():
    
    base_rssi, base_pos = getData('dataBase.xlsx',"Sheet1" ,"A2", "G431")
    test_rssi, test_pos = getData('testPoints.xlsx', "Average",  "A2", "G19")
    training_X = np.array(base_rssi)
    training_Y = np.array(base_pos)
    test_X = np.array(test_rssi)
    reg = MLPRegressor(solver='lbfgs', activation='identity', hidden_layer_sizes=(100,))
    reg.fit(training_X, training_Y)
    for i in range(0,18):
        start = time.time()
        pred_y_test = reg.predict(test_X[i].reshape(1,-1))
        duration = time.time() - start
        error = np.sqrt((pred_y_test[0][0] - test_pos[i][0])**2 + (pred_y_test[0][1] - test_pos[i][1])**2)
        data = []
        data.extend(test_pos[i])
        data.extend(pred_y_test[0])
        data.append(duration)
        data.append(error)
        storeData(data,"FingerNN")
        
if __name__== "__main__":
        main()