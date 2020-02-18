#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 11:37:48 2020

@author: tiago
"""

import os
import sys
import time
import numpy as np
from openpyxl import load_workbook
from scipy.optimize import minimize

x           = [4.4, 2.2, 0, 6.6, 0, 6.6]
y           = [2.6,13.0,6.5, 10.4, 3.9, 7.8]
h           = [0.76, 1.7, 1.65, 1.17, 2.02, 1.52]
distances   = []

def mse(var):
	sum = 0
	for i in range(6):
		sum = sum + ( (x[i] - var[0])**2 + (y[i] - var[1])**2 + (h[i] - 0.73)**2 - distances[i]**2)**2
	return sum

def getRealPosition():
    
	x0  = np.array([1.0, 1.0])
	res = minimize(mse, x0, method='BFGS', options={'gtol': 1e-8})
	return res.x


def collectRSSI(position):
    
	wifis       = ["TiagoLocalizacao1", "TiagoLocalizacao2", "TiagoLocalizacao0", "TiagoLocalizacao3", "TiagoLocalizacao4", "LSC_HoneyPot"]

	t1 = '"signal:|SSID:"'
	t3 = '\\t'.join(('"s/', 'signal: //"'))
	t4 = '"\\n"'
	t5 = '\\t'.join(('"s/', 'SSID: //"'))
	t6 = "'{ORS = (NR % 2 == 0)? " + t4 + ' : ' + '" "' + "; print}'"
	cmd = "sudo iw dev wlan0 scan | egrep " + t1 + " | sed -e " + t3 + " -e " + t5 + " | awk " + t6 + " | sort"
    
    for i in range(10):
        lssi = []
        print("Collecting data from network "+wifi)
        for wifi in wifis:
		 strcmd= os.popen(cmd).readlines()
			for j in range(0,len(strcmd)):
				if wifi in strcmd[j]:
					line = strcmd[j].split()
					l_rssi.append(line[0])
					break
			print(l_rssi)
			time.sleep(2)
		storePosition(position, l_rssi, wifi)
        

def storePosition(position,data,sheetName):
	path    = "realPosition.xlsx"
	wbk     = load_workbook(path)
	page    = wbk[sheetName]
	rowData = []
	rowData.extend(position)
	rowData.extend(data)
	page.append(rowData)
	wbk.save(path)
    
# sys.argv[1...7] = distances of 6 networks
def main():
	
    # collect distances
	for i in range(1,7):
		distances.append(float(sys.argv[i]))
        
	position = getRealPosition()
	storePosition(position,distances,"Sheet1")
	collectRSSI(position)

if __name__== "__main__":
        main()
