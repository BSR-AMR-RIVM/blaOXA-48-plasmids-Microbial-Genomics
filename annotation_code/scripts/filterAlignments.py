# import command line interpretation
import sys

TXT = sys.argv[1]

with open(TXT, 'r') as f:
    for line in f:
         # split the lines to acces the alignment length 
         # lineSplit[9] = identity %
         # only if identity is higher than 99% the hit is accepted
         # in future iterations it ould be wise to take alignment-, query- and subject length in account
        lineSplit = line.split("\t")
        idPercentage = int(float(lineSplit[9]))
        if idPercentage > 99:
            print(line, end='')
        else:
            next