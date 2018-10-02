#!/usr/bin/env python3
import numpy as np

def main():
	i = 0
	n = 10
	x = 119.0
	
	# we can use numpy to declare arrays quickly
	
	y = np.zeros(n,dtype=float) #declares 10 zeros as floats using np
	
	# we can use for loops ot iterate with a variable
	
	for i in range(n):    #i in range [0, n-1]
		y[i] = 2.0 * float(i) +1. #set y = 2i+1 as floats
		
	# we can also simply iterate through a vairable
	
	for y_element in y:
		print(y_element)
		
if __name__ == "__main__":
	main()