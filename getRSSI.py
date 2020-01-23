import os
import sys
import time

def stDeviation(list, avg):
        std = 0
        for num in list:
                std = std +  (num - avg)**2
        return (std/(len(list)-1))**(0.5)

def main():

        wifi = sys.argv[1]
        dist = sys.argv[2]
        n    = int(sys.argv[3])

        f= open(wifi+"-"+dist+".txt","a")
        f.write("Name: " + wifi + " Distance: " + dist + "cm " + "Number = " + str(n) + "\n")

        t1 = '"signal:|SSID:"'
        t3 = '\\t'.join(('"s/', 'signal: //"'))
        t4 = '"\\n"'
        t5 = '\\t'.join(('"s/', 'SSID: //"'))
        t6 = "'{ORS = (NR % 2 == 0)? " + t4 + ' : ' + '" "' + "; print}'"
        cmd = "sudo iw dev wlan0 scan | egrep " + t1 + " | sed -e " + t3 + " -e " + t5 + " | awk " + t6 + " | sort"
        avg = 0
        list = []
        for j in range(0,n):
                strcmd  = os.popen(cmd).readlines()
                time.sleep(1)   
                for i in range(0,len(strcmd)):
                        if wifi in strcmd[i]:
                                line = strcmd[i].split()
                                f.write(line[0]+"\n")
				break
                time.sleep(4)

        avg = avg/(1.0*n)
        std = stDeviation(list, avg)
        f.write("Average: " + str(avg)+"\n")
        f.write("Standard Deviation: " + str(std) + ".\n")
        f.close()

if __name__== "__main__":
        main()


