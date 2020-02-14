#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 16:23:01 2020

@author: mister-c
"""

import os

def main():
    
    i = 0
    f = open("count.txt", "w")
    while(True):
        i = i + 1
        f = open("count.txt", "a")
        os.system("python CircularAlgorithm.py")        
        f.write(str(i)+"\n")
        f.close()
        
if __name__== "__main__":
        main()