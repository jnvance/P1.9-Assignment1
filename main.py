import sys

if __name__ == '__main__':
	try:
		print(int(sys.argv[1]))
	except (IndexError):
		print("Please provide integer input")
		raise
		