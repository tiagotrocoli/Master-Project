#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 22:20:53 2020

@author: tiago
"""

import os
import sys
import time
from openpyxl import load_workbook

path = "../Data/"

def storeData(data,sheetName):
    doc    = "testPoints.xlsx"
    wbk     = load_workbook(path+doc)
    page    = wbk[sheetName]
    page.append(data)
    wbk.save(path+doc)

def main():

    n = 2
    x0 = float(sys.argv[1])
    y0	= float(sys.argv[2])
    
    cmd = "iwlist scan | grep -e ESSID -e level"
    wifis = ["TiagoLocalizacao1", "TiagoLocalizacao2", "TiagoLocalizacao0", "TiagoLocalizacao10", "TiagoLocalizacao11", "TiagoLocalizacao12"]
	
    i = 0
    data = []
    data.append(x0)
    data.append(y0)
    time.sleep(5)
    for wifi in wifis:	

        print("Processing network "+wifi+" ...")
	
        strcmd  = os.popen(cmd).readlines()
		
        avg = 0
        for j in range(0,n):
                for k in range(0,len(strcmd)):
                    if wifi in strcmd[k]:
                            start = strcmd[k-1].find("-")
                            end = strcmd[k-1].find("d")
                            avg = avg + float(strcmd[k-1][start:end])
                            break                           
                time.sleep(1)

        i = i + 1
        data.append(avg/(1.0*n))
    print(data)
    storeData(data,"Experiment2")
    print("End.")

if __name__== "__main__":
        main()