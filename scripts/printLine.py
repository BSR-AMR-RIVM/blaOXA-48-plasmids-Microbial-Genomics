# quick code to print the lines that starts with >
import sys
FILE = sys.argv[1]

with open(FILE, 'r') as f:
	count = 0
	for line in f:
		count =+ 1
		if line.startswith(">"):
			newLine = line.split(' ')
			if len(newLine) < 3:
				print(newLine)
	print(count)