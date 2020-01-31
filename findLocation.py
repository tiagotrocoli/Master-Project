import os
import sys
import csv

def makeHeader():    
    
    header     = ["Real Position"]
    position    = ["Est. Position1", "Est. Position2", "Est. Position3","Est. Position4", "Est. Position5"]
    time        = ["Time1", "Time2", "Time3", "Time4", "Time5"]
    
    header.extend(position)
    header.extend(time)
    
    return header

def realLocalization(algo):
    algo = sys.argv[1]
	os.system("g++ " + algo + "/*.cpp " + "-o " + algo +"/output" )
	result = os.popen("./" + algo + "/output").readlines()
	print(result)

def estimatedLocalization(algo):
    algo = sys.argv[1]
    os.system("g++ " + algo + "/*.cpp " + "-o " + algo +"/output" )
    result = os.popen("./" + algo + "/output").readlines()
    print(result)

def getRSSIs():
    

def main():

	#algo = sys.argv[1]
	#os.system("g++ " + algo + "/*.cpp " + "-o " + algo +"/output" )
	#result = os.popen("./" + algo + "/output").readlines()
	#print(result)
    
    header  = makeHeader()    
    n       = len(sys.argv) - 6
    # get distance from argv
    
    for i in range(1,n):
        l_time      = []
        l_position  = []
        algo        = sys.argv[i]
        with open("Results/" + algo + '.csv', 'w+') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            real_pos = realLocalization(algo)
            for i in range(5):
                position, time = estimatedLocalization(algo)
                l_position.append(position)
                l_time.append(time)
             
                
if __name__== "__main__":
	main()
