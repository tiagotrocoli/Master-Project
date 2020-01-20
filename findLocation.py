import os
import sys

def main():

	algo = sys.argv[1]

	os.system("g++ " + algo + "/*.cpp " + "-o " + algo +"/output" )
	result = os.popen("./" + algo + "/output").readlines()
	print(result)

if __name__== "__main__":
	main()
