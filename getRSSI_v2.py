import os
import sys
import time
import math

def stDeviation(list, avg):
        std = 0
        for num in list:
                std = std +  (num - avg)**2
        return (std/(len(list)-1))**(0.5)

def createDirectory():

	for i in range(6):
		f.write()

def main():
	
	dist = []
	
	n    	= int(sys.argv[1])
	x0	= float(sys.argv[2])
	y0	= float(sys.argv[3])
	h0 	= float(sys.argv[4])	
	
	x = [4.4, 2.2, 0, 6.6, 0, 6.6]
	y = [2.6,13.0,6.5, 10.4, 3.9, 7.8]
	h = [0.76, 1.7, 1.65, 1.17, 2.02, 1.52]
	
	for i in range(6):
		dist.append(math.sqrt((x[i]-x0)**2 + (y[i]-y0)**2 + (h[i]-h0)**2))
	
	t1 = '"signal:|SSID:"'
	t3 = '\\t'.join(('"s/', 'signal: //"'))
	t4 = '"\\n"'
	t5 = '\\t'.join(('"s/', 'SSID: //"'))
	t6 = "'{ORS = (NR % 2 == 0)? " + t4 + ' : ' + '" "' + "; print}'"
	cmd = "sudo iw dev wlan0 scan | egrep " + t1 + " | sed -e " + t3 + " -e " + t5 + " | awk " + t6 + " | sort"	

	num = ["3", "6", "2", "4", "7", "8"]
	wifis = ["TiagoLocalizacao1", "TiagoLocalizacao2", "TiagoLocalizacao0", "TiagoLocalizacao3", "TiagoLocalizacao4", "LSC_HoneyPot"]
	
	f= open("Localize"+str(x0)+str(y0)+".txt","w")
	f.write(str(x0) + " " +str(y0)+ " " + str(h0) + "\n")
	f.write(str(n)+"\n")
	
	i = 0

	for wifi in wifis:	
		
		print("Processing network "+wifi+" ...")
	
		strcmd  = os.popen(cmd).readlines()
		if not any(wifi in line for line in strcmd):
			i = i + 1
			continue
		
		f.write(wifis[i] + " " + str(dist[i])+"\n")
		for j in range(0,n):
		        strcmd  = os.popen(cmd).readlines() 
		        for k in range(0,len(strcmd)):
		                if wifi in strcmd[k]:
		                        line = strcmd[k].split()
		                        f.write(line[0]+"\n")
					break
		        time.sleep(2)

		i = i + 1
		print("End.")

	f.close()

if __name__== "__main__":
        main()
