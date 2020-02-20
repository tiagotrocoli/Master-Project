#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 16:08:09 2020

@author: mister-c
"""
import socket
import pickle
import sys
import time
import math
import locale
from openpyxl import load_workbook

x           = [4.4, 2.2, 0, 6.6, 0, 6.6]
y           = [2.6,13.0,6.5, 10.4, 3.9, 7.8]
h           = [0.76, 1.7, 1.65, 1.17, 2.02, 1.52]

path = "../Data/"

def getData(doc, page, ini, end):
    wbk     = load_workbook(path+doc)
    sheet   = wbk[page]
    cells   = sheet[ini : end]
    
    position = []
    row = []

    i = -1
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    for pos1, pos2, c1, c2, c3, c4, c5, c6 in cells:
        i = i + 1
        position.append([])
        position[i].append(locale.atof(pos1.value))
        position[i].append(locale.atof(pos2.value))
        row.append([locale.atof(c1.value), locale.atof(c2.value), locale.atof(c3.value), locale.atof(c4.value), locale.atof(c5.value)])
    
    return row, position

def fingerpriting(rssi_base,base_pos,rssi_test,pos_test,n):
    
    cost = []
    # execute Fingerpriting and calculate its processing time
    start = time.time()
    for i in range(43):
        cost.append((rssi_test[0] - rssi_base[i][0])**2 + (rssi_test[1] - rssi_base[i][1])**2 + (rssi_test[2] - rssi_base[i][2])**2 + (rssi_test[3] - rssi_base[i][3])**2 + (rssi_test[4] - rssi_base[i][4])**2)
    # sort cost and index of base_pos accordingly
    pos = [x for _,x in sorted(zip(cost,base_pos))]
    x = y = 0
    for j in range(n):
        x = x + pos[j][0]
        y = y + pos[j][1]
    x = x/(1.0*n)
    y = y/(1.0*n)
    duration = time.time() - start
    estimate = [round(x, 2),round(y, 2)]
    # calculate error
    error = math.sqrt((estimate[0] - pos_test[0])**2 + (estimate[1] - pos_test[1])**2)
    # put them together
    data = [pos_test[0], pos_test[1]]
    data.extend(estimate)
    data.append(duration)
    data.append(error)
    
    return data

def main():
    
    # next create a socket object 
    s = socket.socket()          
    print("Socket successfully created")  
    # reserve a port on your computer in our 
    # case it is 12345 but it can be anything 
    port = 12225                  
    # Next bind to the port 
    # we have not typed any ip in the ip field 
    # instead we have inputted an empty string 
    # this makes the server listen to requests  
    # coming from other computers on the network 
    s.bind(('', port))         
    print("socket binded to %s" %(port))  
    # put the socket into listening mode 
    s.listen(1)      
    print("socket is listening")            
    # Establish connection with client. 
    channel, addr = s.accept()
    print('Got connection from', addr) 
      
    rssi_base, base_pos = getData('dataBase.xlsx',"Average" ,"A2", "H44")
    rssi_test, test_pos = getData('testPoints.xlsx', "Average",  "A2", "H19")
    
    while True:
        for k in range(0,18):
            recd_data = channel.recv( 1024 )
            recd_data = pickle.loads(recd_data)
            send_data = fingerpriting(rssi_base,base_pos,recd_data,test_pos[k],4)
            channel.send(pickle.dumps(send_data))
    channel.close()
        
if __name__== "__main__":
        main()
