# import command line interpretation
import sys

FILE = sys.argv[1]

# only print the records that contain hypothetical
# this script is used beacause only the hypothetical proteins get aligned with blastp later
with open(FILE, "r+") as f:
    for line in f:
        if 'hypothetical' in line:
            print(line, end='')
        else:
            next