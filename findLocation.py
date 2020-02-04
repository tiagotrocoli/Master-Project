import os
import sys
import csv

wifis = ["TiagoLocalizacao1", "TiagoLocalizacao2", "TiagoLocalizacao0", "TiagoLocalizacao3", "TiagoLocalizacao4", "LSC_HoneyPot"]

def makeHeader():    
    
    header     = ["Real Position"]
    position    = ["Est. Position1", "Est. Position2", "Est. Position3","Est. Position4", "Est. Position5"]
    time        = ["Time1", "Time2", "Time3", "Time4", "Time5"]
    
    header.extend(position)
    header.extend(time)
    
    return header


def realLocalization(algo, l_distance):
    
    entry = "1 "
    for d in l_distance:
        entry = entry + d
    
    os.system("g++ " + algo + "/*.cpp " + "-o " + algo +"/output" )
    result = os.popen("./" + algo + "/output " + entry).readlines()
    print(result)

# l_rssi is str or number 
def estimatedLocalization(algo, l_rssi):
    
    entry = "2 "
    for rssi in l_rssi:
        entry = entry + rssi
    
    os.system("g++ " + algo + "/*.cpp " + "-o " + algo +"/output" )
    result = os.popen("./" + algo + "/output " + entry).readlines()
    print(result)


def getRSSIs():
    
    t1 = '"signal:|SSID:"'
    t3 = '\\t'.join(('"s/', 'signal: //"'))
    t4 = '"\\n"'
    t5 = '\\t'.join(('"s/', 'SSID: //"'))
    t6 = "'{ORS = (NR % 2 == 0)? " + t4 + ' : ' + '" "' + "; print}'"
    cmd = "sudo iw dev wlan0 scan | egrep " + t1 + " | sed -e " + t3 + " -e " + t5 + " | awk " + t6 + " | sort"
    
    l_rssi = []
    strcmd  = os.popen(cmd).readlines()
    for wifi in wifis:
        for k in range(0,len(strcmd)):
            if wifi in strcmd[k]:
                line = strcmd[k].split()
                l_rssi.append(line[0])
    
    return l_rssi


def getDistances():
    
    l_distances = []
    for wifi in wifis:
        l_distances.append(input("Rssi of "+wifi+": "))
    return l_distances


def main():

	#algo = sys.argv[1]
	#os.system("g++ " + algo + "/*.cpp " + "-o " + algo +"/output" )
	#result = os.popen("./" + algo + "/output").readlines()
	#print(result)
    
    header      = makeHeader()    
    n           = len(sys.argv) - 6
    l_distance  = getDistances()
    
    # for each location method, do...
    for i in range(1,n):
        l_time      = []
        l_position  = []
        algo        = sys.argv[i]
        with open("Results/" + algo + '.csv', 'w+') as file:
            # find real position
            writer = csv.writer(file)
            writer.writerow(header)
            real_pos = realLocalization(algo, l_distance)
            # find estimated postion 5 times
            for i in range(5):
                l_rssi = getRSSIs()
                position, time = estimatedLocalization(algo, l_rssi)
                l_position.append(position)
                l_time.append(time)
             
                
if __name__== "__main__":
	main()
