# import SeqIO from BioPython to recognize and parse the entries in the genbank files
from Bio import SeqIO
# import command line interpretation
import sys

FILE = sys.argv[1]

# for each entry in the .gbk file, parse all the headers and also the sequence in a record.
try:
    for record in SeqIO.parse(FILE, "genbank"):
        for i in record.features:
            if i.type=="CDS":
                assert len(i.qualifiers['translation'])==1
                print (i.qualifiers)
except:
    print("Error in parsing records, please take a look at the record options and the qualifiers.")