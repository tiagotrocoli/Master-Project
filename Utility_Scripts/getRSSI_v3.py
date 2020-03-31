#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 19:42:27 2020

@author: tiago
"""

import os
import sys
import time
from openpyxl import load_workbook

path = "../Data/"

def storeData(data,sheetName):
    doc    = "dataBase.xlsx"
    wbk     = load_workbook(path+doc)
    page    = wbk[sheetName]
    page.append(data)
    wbk.save(path+doc)

def main():

    n = 10
    x0 = float(sys.argv[1])
    y0	= float(sys.argv[2])
    
    t1 = '"signal:|SSID:"'
    t3 = '\\t'.join(('"s/', 'signal: //"'))
    t4 = '"\\n"'
    t5 = '\\t'.join(('"s/', 'SSID: //"'))
    t6 = "'{ORS = (NR % 2 == 0)? " + t4 + ' : ' + '" "' + "; print}'"
    cmd = "sudo iw dev wlan0 scan | egrep " + t1 + " | sed -e " + t3 + " -e " + t5 + " | awk " + t6 + " | sort"	

    wifis = ["TiagoLocalizacao1", "TiagoLocalizacao2", "TiagoLocalizacao0", "TiagoLocalizacao10", "TiagoLocalizacao11", "TiagoLocalizacao12"]
	
    i = 0
    data = []
    data.append(x0)
    data.append(y0)
    for wifi in wifis:	

        print("Processing network "+wifi+" ...")
	
        strcmd  = os.popen(cmd).readlines()
        if not any(wifi in line for line in strcmd):
            i = i+ 1
            continue
		
        avg = 0
        for j in range(0,n):
                strcmd = os.popen(cmd).readlines() 
                for k in range(0,len(strcmd)):
                    if wifi in strcmd[k]:
                            line = strcmd[k].split()
                            avg = avg + float(line[0])
                            break                           
                time.sleep(1)

        i = i + 1
        data.append(avg/(1.0*n))
    storeData(data,"Experiment2")
    print("End.")

if __name__== "__main__":
        main()
