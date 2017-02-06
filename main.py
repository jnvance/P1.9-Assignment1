import sys
import numpy as np

f_list = { 1: lambda x: x }

if __name__ == '__main__':
	try:
		f = f_list[int(sys.argv[1])]
	except (IndexError,ValueError,KeyError):
		print("Please provide integer input")
		raise
	
	xval = np.arange(-5.0,+5.1,0.1)
	yval = f(xval)

	print(xval)
	print(yval)