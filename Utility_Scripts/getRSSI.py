import os
import sys
import time

def stDeviation(list, avg):
        std = 0
        for num in list:
                std = std +  (num - avg)**2
        return (std/(len(list)-1))**(0.5)

def main():
	
	dist = []
	
	n    = int(sys.argv[1])
	dist.append(int(sys.argv[2]))
	dist.append(int(sys.argv[3]))
	dist.append(int(sys.argv[4]))
	dist.append(int(sys.argv[5]))
	dist.append(int(sys.argv[6]))
	dist.append(int(sys.argv[7]))

	t1 = '"signal:|SSID:"'
	t3 = '\\t'.join(('"s/', 'signal: //"'))
	t4 = '"\\n"'
	t5 = '\\t'.join(('"s/', 'SSID: //"'))
	t6 = "'{ORS = (NR % 2 == 0)? " + t4 + ' : ' + '" "' + "; print}'"
	cmd = "sudo iw dev wlan0 scan | egrep " + t1 + " | sed -e " + t3 + " -e " + t5 + " | awk " + t6 + " | sort"	

	num = ["3", "6", "2", "4", "7", "0"]
	wifis = ["TiagoLocalizacao1", "TiagoLocalizacao2", "TiagoLocalizacao0", "TiagoLocalizacao3", "TiagoLocalizacao4", "LSC_HoneyPot"]
	
	for wifi in wifis:	
		
		print("Processing network "+wifi+" ...")

		strcmd  = os.popen(cmd).readlines()
		if not any(wifi in line for line in strcmd)
			continue

		f= open(wifi+"-"+str(dist[i])+".txt","w")
		
		#avg = 0
		#list = []
		for j in range(0,n):
		        strcmd  = os.popen(cmd).readlines() 
		        for i in range(0,len(strcmd)):
		                if wifi in strcmd[i]:
		                        line = strcmd[i].split()
		                        f.write(line[0]+"\n")
					break
		        time.sleep(5)

		#avg = avg/(1.0*n)
		#std = stDeviation(list, avg)
		#f.write("Average: " + str(avg)+"\n")
		#f.write("Standard Deviation: " + str(std) + ".\n")
		f.close()
		i = i + 1

		print("End.")


if __name__== "__main__":
        main()


