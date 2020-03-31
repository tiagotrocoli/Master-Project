#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 22:18:58 2020

@author: tiago
"""

import os

os.system("sudo apt-get update")
#os.system("sudo apt-get dist-upgrade")
print("1")
os.system("sudo apt install dnsmasq hostapd")
os.system("sudo systemctl stop dnsmasq")
os.system("sudo systemctl stop hostapd")
print("2")
os.system("sudo cat dhcp.txt >> /etc/dhcpcd.conf")
print("3")
os.system("sudo service dhcpcd restart")
print("4")
os.system("sudo mv /etc/dnsmasq.conf /etc/dnsmasq.conf.orig")
print("5")
os.system("sudo cat dnsmasq.txt >> /etc/dnsmasq.conf")
print("6")
os.system("sudo systemctl start dnsmasq")
print("7")
os.system("sudo cat network.txt >> /etc/hostapd/hostapd.conf")
print("8")
os.system("sudo nano /etc/default/hostapd")
print("9")
os.system("sudo systemctl unmask hostapd")
os.system("sudo systemctl enable hostapd")
os.system("sudo systemctl start hostapd")
print("10")
os.system("sudo systemctl status hostapd")
os.system("sudo systemctl status dnsmasq")
print("11")
os.system("sudo nano /etc/sysctl.conf")
print("12")
os.system("sudo iptables -t nat -A  POSTROUTING -o eth0 -j MASQUERADE")
os.system('sudo sh -c "iptables-save > /etc/iptables.ipv4.nat"')
print("13")
os.system("sudo cat iptable.txt >> /etc/rc.local")
