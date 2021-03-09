# import command line interpretation
import sys
FILE = sys.argv[1]

# remove the remaining lines with hypothetical_protein_# and replace them with the original notation
with open(FILE, "r+") as f:
    for line in f:
        if '/product="hypothetical_protein_' in line:
            print('                     /product="hypothetical protein"')
        else:
            print(line, end = '')