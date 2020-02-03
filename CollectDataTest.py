#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 11:37:48 2020

@author: tiago
"""

import os
import sys
from openpyxl import load_workbook

wifis   = ["TiagoLocalizacao1", "TiagoLocalizacao2", "TiagoLocalizacao0", "TiagoLocalizacao3", "TiagoLocalizacao4", "LSC_HoneyPot"]
num     = ["3", "6", "2", "4", "7", "8"]
path    = "Test/realPosition.xlsx"

def getRealPosition(distances):
    
    inputs = " ".join(distances)
    os.system("cd HyperbolicAlgorithm/")
    os.system("g++ *.cpp -o output" )
    result = os.popen("./output 1 " + inputs).readlines()
    
    return [result[0], result[1]]

def collectDistances():
    distances = []
    for i in range(1,7):
        distances.append(sys.argv[i]);
    return distances

# =============================================================================
# def collectRSSI(wifi):
#     
#     t1 = '"signal:|SSID:"'
#     t3 = '\\t'.join(('"s/', 'signal: //"'))
#     t4 = '"\\n"'
#     t5 = '\\t'.join(('"s/', 'SSID: //"'))
#     t6 = "'{ORS = (NR % 2 == 0)? " + t4 + ' : ' + '" "' + "; print}'"
#     cmd = "sudo iw dev wlan0 scan | egrep " + t1 + " | sed -e " + t3 + " -e " + t5 + " | awk " + t6 + " | sort"
#     
#     for i in range(5):
#         print("Collecting data from network "+"wifi")
#         strcmd  = os.popen(cmd).readlines()        
#         
# =============================================================================
def storePosition(position, distances):
    wbk     = load_workbook(path)
    page    = wbk.get_active_sheet("Sheet1")
    rowData = []
    rowData.extend(position)
    rowData.extend(distances)
    page.append(rowData)
    wbk.save(path)
    
# sys.argv[1...7] = distances of 6 networks
def main():
	
    distances   = collectDistances()
    position    = getRealPosition(distances)
    storePosition(position,distances)
    

if __name__== "__main__":
        main()