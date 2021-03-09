# import to interpret command line given input when using the coding language Python.
# for example, the process in this code is invoked by typing 'python adjustNames.py inputfule' 
# with the usage of sys, sys.arv[0] = adjustNames.py, sys.arv[1] = the first inputfile.

# import regular expression interpretation
import re
import sys
FILE = sys.argv[1]

with open(FILE, "r+") as f:
    count = 0
    for line in f:
        if '/gene=' in line:
            result = re.sub(r"_[\d]", "", line)
            print(result, end = '')
        # a temporary solution until a way is found to assign the correct products to the .gbk files
        elif '_no_value' in line:
            next
        elif '/product="hypothetical protein"' in line:
            count += 1
            # the exessive amounts of spaces is due to the genbank format.
            print('                     /product="hypothetical_protein_' + str(count) + '"')
        else:
            print(line, end = '')
			