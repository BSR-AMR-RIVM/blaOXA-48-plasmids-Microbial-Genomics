# import to interpret command line given input when using the coding language Python.
# for example, the process in this code is invoked by typing 'python resfinder_dbUpdate.py inputfule' 
# with the usage of sys, sys.arv[0] = plasmidfinder_dbUpdate.py, sys.arv[1] = the first inputfile and sys.arv[2] = the second inputfile.
import sys
FILE = sys.argv[1]

# FILE reffers to the input file given from the command line and interpreted by sys.
# furthermore the line in the file are being read one by one and handled accordingly in the rest of the code.
with open(FILE, 'r') as e:
	prev = ''
	for line in e:
		line = line.strip('\n')
		if line.startswith(">"):
		
			header = line
			headerStrip = header.strip(">")
			headerSplit = headerStrip.split("_")
			
			# because the lines are split on '_' there occured an issue with genes that had 'NC_' formatted accession codes
			# the following rules checks the content of the columns and assign the columns to the variables accordingly

			# headerSplit[1] (and for some cases headerSplit[2]) consist a numeric value Resfinder adds to the gene names to identify different variations of the same gene.
			# because these variations can also be identified by their accession number, and to preserve the gene name this value will be left out.
			if headerSplit[3] == 'NC' or headerSplit[3] == 'NZ':
				gene = headerSplit[0]
				accession = (headerSplit[3] + '_' + headerSplit[4])
				length = headerSplit[5]
			elif headerSplit[0] == "IncFII(pKPX1)" or headerSplit[0] == "repUS28":
				# origin = "NB" 
				accession = headerSplit[2]
				length = headerSplit[3]
			elif headerSplit[1] == 'Gamma':
				gene = (headerSplit[0] + '_' + headerSplit[1])
				#origin = headerSplit[2]
				accession = headerSplit[3]
				length = headerSplit[4]
			else:
				gene = headerSplit[0]
				#origin = headerSplit[2]
				accession = headerSplit[3]
				length = headerSplit[4]
			
			# prokka's format for the genbank entries
			print("//" + "\n")
			print("LOCUS       RIVM " + length + " bp")
			print("FEATURES Location/Qualifiers")
			# organism etc werd niet goed meegenomen in prokka
			# print("  source " + "1.." + length )
			# print('         /organism="' + origin + '"')
			print("     CDS " + "1.." + length )
			print('         /gene="' + gene + '"')
			print('         /codon_start=1')
			print('         /transl_table=11')
			print('         /product=')						# the product will be left empty until we found a better solution to add this information.
			print('         /protein_id="' + accession + '"')
			
			print("ORIGIN")
			
		else:
			# he header only starts with '>' so automatically the remaining lines contain the sequence
			sequence = ''
			sequence += line
			
			print(sequence.upper())
			