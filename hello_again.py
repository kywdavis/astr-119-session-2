#!/usr/bin/env Python3

#include the Numpy library
import numpy as np

#define the main
def main():

	i = 0 #declare an integer i, set to 0
	x = 119.0 #floating point variable set to 119
	
	for i in range(120):  #loops i from 0 to 120
		
		if ((i%2) == 0):  #if i is even(remainder when divided by 2 is zero), add 3 to x
			x += 3 #x = x + 3
		else:    #otherwise, subtract 5 from x
			x -= 5 #x = x - 5
			
	#lets print a string of x in scientific notation 3 digits, 2 after decimal hence 3.2
	s = "%3.2e" % x
	
	print(s)
	
#now the rest of the program
if __name__ == "__main__": #if the main program exists, run it
	main()