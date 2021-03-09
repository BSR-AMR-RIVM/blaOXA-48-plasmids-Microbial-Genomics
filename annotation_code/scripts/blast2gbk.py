# import command line interpretation
import sys

BLAST = sys.argv[1]
GBK = sys.argv[2]

with open(BLAST, "r+") as blast, open(GBK, "r+") as gbk:
    hitList = []
    # create an empty list to append all blast hits
    for line1 in blast:
        splitLine = line1.split('\t')[0:2]
        stripLine = splitLine.strip("MULTISPECIES: ")
        hitList += stripLine

    # compare the lines in the annotation file to the blast file and match on sample key hitList[0]
    # when a match is found the whole line gets overwitten by a new product with the blast hit
    # after this is done the list will remove these values and continue searching for the next match
    for line2 in gbk:
        try:
            if hitList != [] and hitList[0] in line2:
                print('                     /product="'+ hitList[1] + '"')
                del hitList[:2]
            else:
                print(line2, end = '')
        except IndexError:
            print("Index error, please take a look at the process of the value deletion within the list")