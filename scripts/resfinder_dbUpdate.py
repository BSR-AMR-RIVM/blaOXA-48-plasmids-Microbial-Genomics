# import to interpret command line given input when using the coding language Python.
# for example, the process in this code is invoked by typing 'python resfinder_dbUpdate.py inputfule' 
# with the usage of sys, sys.arv[0] = resfinder_dbUpdate.py and sys.arv[1] = the inputfile.
import sys
FILE = sys.argv[1]

# FILE reffers to the input file given from the command line and interpreted by sys.
# furthermore the line in the file are being read one by one and handled accordingly in the rest of the code.
with open(FILE, 'r') as f:
	prev = ''
	for line in f:
		line = line.strip('\n')
		if line.startswith(">"):
		
			header = line
			headerStrip = header.strip(">")
			headerSplit = headerStrip.split("_")
			
			# because the lines are split on '_' there occured an issue with genes that had 'NC_' formatted accession codes
			# the following rules checks the content of the columns and assign the columns to the variables accordingly
			if headerSplit[2] == 'NC' or headerSplit[2] == 'NZ' or headerSplit[2] == 'ENA' or headerSplit[2] == 'NG':
				gene = headerSplit[0] 
				accession = (headerSplit[2] + '_' + headerSplit[3])
				length = headerSplit[4]

			# after the 29/01/2019 update of the resfinder_db, the new file glycopeptide.fsa prompted some new issues
			# the following rules checks the content of the columns and assign the columns to the variables accordingly
			elif headerSplit[1] == 'bc' or headerSplit[1] == 'PT' or headerSplit[1] == 'PA' or headerSplit[1] == 'C2': 
				gene = (headerSplit[0] + '_' + headerSplit[1])
				accession = headerSplit[3]
				length = headerSplit[4]

			# the header allocation without the exceptions as stated above.
			# headerSplit[1] (and for some cases headerSplit[2]) consist a numeric value Resfinder adds to the gene names to identify different variations of the same gene.
			# because these variations can also be identified by their accession number, and to preserve the gene name this value will be left out.
			else:
				gene = headerSplit[0]
				accession = headerSplit[2]
				length = headerSplit[3]
			
			# prokka's format for the genbank entries, it is space specific.
			print("//" + "\n")
			print("LOCUS       RIVM " + length + " bp")
			print("FEATURES Location/Qualifiers")
			print("     CDS " + "1.." + length )
			print('         /gene="' + gene + '"')
			print('         /codon_start=1')
			print('         /transl_table=11')
			print('         /product=')						# the product will be left empty until we found a better solution to add this information.
			print('         /protein_id="' + accession + '"')
			print("ORIGIN")
			
		else:
			# the header only starts with '>' so automatically the remaining lines contain the sequence
			sequence = ''
			sequence += line
			
			print(sequence.upper())
			

