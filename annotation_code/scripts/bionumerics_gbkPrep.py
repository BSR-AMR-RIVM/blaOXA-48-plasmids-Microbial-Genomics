# import to interpret command line given input when using the coding language Python.
# for example, the process in this code is invoked by typing 'python bionumerics_gbkPrep.py inputfule' 
# with the usage of sys, sys.arv[0] = bionumerics_gbkPrep.py, sys.arv[1] = the first inputfile.

# version 2.0

import sys
FILE = sys.argv[1]

fileStrip = FILE.strip("output/prokka/")
fileSplit = fileStrip.split("_")

key = fileSplit[0]		# reffers to BioNumerics key
organism = fileSplit[1]

#! creates the new lines when the old lines are found, te rest of the lines can be printed without any issue
with open(FILE, "r+") as f:
	count = 0
	for line in f:
		if line.startswith("  ORGANISM"):
            # in the next version, it would be optimal to note the full name of the organism after recognizing the three letter code, for example Eco == Escherichia coli
			newORGANISM = ("  ORGANISM  " + str(organism))
			print(newORGANISM)
		else:
			print(line, end = '')