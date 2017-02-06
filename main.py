# -*- coding: utf-8 -*-

import sys
import numpy as np
import matplotlib.pyplot as plt

f_list = { 	1: lambda x: x ,
			2: np.exp ,
			3: lambda x: np.sqrt(np.abs(x)) }

usage = "\
Wrong or missing input 			\n\
Usage: python main.py [<key>]	\n\
┌───────┬───────────────────┐	\n\
│  key  │   function        │	\n\
├───────┼───────────────────┤	\n\
│   1   │  f(x) = x         │	\n\
│   2   │  f(x) = exp(x)    │	\n\
│   3   │  f(x) = sqrt(|x|) │	\n\
└───────┴───────────────────┘"

if __name__ == '__main__':
	try:
		f = f_list[int(sys.argv[1])]
	except (IndexError,ValueError,KeyError):
		raise ValueError(usage)
	
	xval = np.arange(-3.0,+3.1,0.1)
	yval = f(xval)

	plt.plot(xval,yval)
	plt.grid()
	plt.xlabel('$x$')
	plt.ylabel('$f(x)$')
	plt.show()