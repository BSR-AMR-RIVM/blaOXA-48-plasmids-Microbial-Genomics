# import to interpret command line given input when using the coding language Python.
# for example, the process in this code is invoked by typing 'python resfinder_dbUpdate.py inputfule' 
# with the usage of sys, sys.arv[0] = resfinder_dbUpdate.py and sys.arv[1] = the inputfile.
import sys
import re
FILE = sys.argv[1]

# FILE reffers to the input file given from the command line and interpreted by sys.
# furthermore the line in the file are being read one by one and handled accordingly in the rest of the code.
with open(FILE, 'r') as f:
	for line in f:
		line = line.strip('\n')
		gene = '' 
		organism = '' 
		product = ''
		try:
			if line.startswith(">"):
				# Here we remove al the non-printing ASCII characters and the > at the start of the line
				header = line
				header2 = re.split(r'[\x00-\x1f\x7f-\x9f]', header)[0]
				headerStrip = header2.strip(">")
				headerSplit = headerStrip.split(" ", 1)
			
				# NCBI starts with an accessioncode so this is the first to allocate
				accession = headerSplit[0]
			
				# Here we format the original header from NCBI so organism, gene and product can extracted
				orgTemp1 = headerSplit[1]
				orgTemp2 = orgTemp1.rsplit('_',1)[0]
				orgTemp3 = orgTemp2.replace(". ", ".")
				newHeader = orgTemp3.split(' ')
			
				if '.' in newHeader[0] and newHeader[2] != 'gene' or newHeader[2] != 'genes':
					organism = ('"' + newHeader[0] + '"')
					prodTemp = newHeader[3:]
					prodTemp2 = str(prodTemp).replace('[', '').replace(']', '').replace(',', '').replace("'", '')
					product = prodTemp2
				elif '.' in newHeader[0] and newHeader[2] == 'gene' or newHeader[2] == 'genes':
					organism = ('"' + newHeader[0] + '"')
					gene = ('"' + newHeader[1] + '"')
					prodTemp = newHeader[3:]
					prodTemp2 = str(prodTemp).replace('[', '').replace(']', '').replace(',', '').replace("'", '')
					product = prodTemp2
				elif '.' not in newHeader[0] and newHeader[3] != 'gene' or newHeader[3] != 'genes':
					organism = ('"' + newHeader[0] + ' ' + newHeader[1] + '"')
					prodTemp = newHeader[4:]
					prodTemp2 = str(prodTemp).replace('[', '').replace(']', '').replace(',', '').replace("'", '')
					product = prodTemp2
				elif '.' not in newHeader[0] and newHeader[3] == 'gene' or newHeader[3] == 'genes':
					organism = ('"' + newHeader[0] + ' ' + newHeader[1] + '"')
					gene = ('"' + newHeader[2] + '"')
					prodTemp = newHeader[4:]
					prodTemp2 = str(prodTemp).replace('[', '').replace(']', '').replace(',', '').replace("'", '')
					product = prodTemp2
					
				# extract length from original header
				headerStrip2 = header.rsplit("_", 1)
				length = headerStrip2[1]
			
				# prokka's format for the genbank entries, it is space specific.
				print("//" + "\n")
				print("LOCUS       RIVM " + length + " bp")
				print("FEATURES Location/Qualifiers")
				print("     CDS " + "1.." + length )
				print('         /organism=' + organism)					# same applies to this as to gene
				print('         /gene=' + gene)							# gene will need ot be filtered out later then looking at the description
				print('         /codon_start=1')
				print('         /transl_table=11')
				print('         /product=')# + str(product) + '"')
				print('         /protein_id="' + accession + '"')
				print("ORIGIN")
			
			else:
				# the header only starts with '>' so automatically the remaining lines contain the sequence
				sequence = ''
				sequence += line
				print(sequence.upper())
				
		except IndexError:
			next

