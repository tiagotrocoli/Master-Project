#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 22:20:24 2020

@author: tiago
"""
import os
import numpy as np
import matplotlib.pyplot as plt

networks = ['TiagoLocalizacao1','TiagoLocalizacao2','TiagoLocalizacao0','TiagoLocalizacao3', 'TiagoLocalizacao4',"LSC_HoneyPot"]

def removeDuplicate(dist,rssi):
    
    for i in range(len(dist)):
        j = i + 1
        while(j < len(dist)):
            if dist[i] == dist[j]:
                rssi[i].extend(rssi[j])
                rssi.pop(j)
                dist.pop(j)
            else:
                j = j + 1
    
    return (dist, rssi)
    
def main():
    
    rssi = []
    dist = []
    m = len(networks)
    path = 'Data/'
    
    for i in range(m):
        dist.append([])
        rssi.append([])
        k = 0
        for filename in os.listdir(path):
            file  = open(path+filename, "r")
            lines = file.readlines()
            dist[i].append(float(lines[2+11*i].split(" ")[1]))
            rssi[i].append([])
            for j in range(1,11):
                rssi[i][k].append(float(lines[2+11*i+j]))
            k = k + 1
        
        dist[i], rssi[i] = removeDuplicate(dist[i], rssi[i])
        
        plt.figure(figsize=(16.0,12.0))
        for s in range(len(dist[i])):
            plt.plot(dist[i][s],[rssi[i][s]],'ko')
        plt.title(networks[i]+" distance x rssi")
        plt.xlabel("Distance (m)")
        plt.ylabel("RSSI (dBm)")
        plt.savefig(networks[i])
        
if __name__== "__main__":
        main()

