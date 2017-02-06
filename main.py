# -*- coding: utf-8 -*-

import sys
import numpy as np
import matplotlib.pyplot as plt

f_list = { 	1: lambda x: x ,
			2: lambda x: x**2 ,
			3: lambda x: x**3 }

usage = "\
Wrong or missing input 			\n\
Usage: python main.py [<key>]	\n\
┌───────┬───────────────────┐	\n\
│  key  │   function        │	\n\
├───────┼───────────────────┤	\n\
│   1   │  f(x) = x         │	\n\
│   2   │  f(x) = x**2      │	\n\
│   3   │  f(x) = x**3      │	\n\
└───────┴───────────────────┘"

if __name__ == '__main__':
	try:
		f = f_list[int(sys.argv[1])]
	except (IndexError,ValueError,KeyError):
		raise ValueError(usage)

	xval = np.arange(-5.0,+5.1,0.1)
	yval = f(xval)

	plt.plot(xval,yval)
	plt.grid()
	plt.xlabel('$x$')
	plt.ylabel('$f(x)$')
	plt.show()
