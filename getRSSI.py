import os
import sys

def main():

	wifi = sys.argv[1]
	dist = sys.argv[2]
	
	name = "Name: " + wifi + " Distance: " + dist + "m."

	f= open(wifi+"-"+dist+".txt","w+")
	f.write("Name: " + wifi + " Distance: " + dist + "m.\n")

	t1 = '"signal:|SSID:"'
	t3 = '\\t'.join(('"s/', 'signal: //"'))
	t4 = '"\\n"'
	t5 = '\\t'.join(('"s/', 'SSID: //"'))
	t6 = "'{ORS = (NR % 2 == 0)? " + t4 + ' : ' + '" "' + "; print}'"
	cmd = "sudo iw dev wlan0 scan | egrep " + t1 + " | sed -e " + t3 + " -e " + t5 + " | awk " + t6 + " | sort"

	strcmd  = os.popen(cmd).readlines()
	print(strcmd)
	
	for i in len(strcmd):
		if wifi in strcmd[i]:
			str = strcmd[i].split()
			print(str[0] + " " + str[2])
			break			

	f.close()
if __name__== "__main__":
	main()
