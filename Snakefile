#------------------------------------------------------------------------------------
# Name     :	Create reference file from plasmidfinder and resfinder data
#
# Purpose  :    Final version of the create_reference pipeline:
#                - able to combine sequences from Resfinder and Plasmidfinder
#                - able to format .FASTA files to .GB files
#
# Author   :	Dyogo Borst, RIVM
#
# Date     :    22/01/2019
#
# Update   :	05/02/2019
#				resfinder_db got an update on 29/01/2019, multiple resistance 
#				gene were added, for example almost 300 to beta-lactam, and around
#				50 to colistin. vancomycin.fsa got replaced by glycopeptide.fsa.
#------------------------------------------------------------------------------------

resfiles, = glob_wildcards("/mnt/db/amr_annotation_db/db_resfinder/{rfile}.fsa")
plafiles, = glob_wildcards("/mnt/db/amr_annotation_db/plasmidfinder_db/{pfile}.fsa")

rule all:
	input:
		expand("output/reference/ResPlas_Reference_Genes.gb")

# this rule combines all the seperate fasta files into one single fasta file.
# ! hardcoded fasta files from resfinder, when more fasta files will be created in the future it is advised to write a more dynamical approach.
# ! please make sure the sequence is not all written on a single line, the format should be a maximum of 60bp per line (seqkit seq -w 60 input > output).
rule combine_resfinder_fsa:
	input:
		expand("/mnt/db/amr_annotation_db/db_resfinder/{rfile}.fsa", rfile=resfiles)
	output:
		"output/resfinder_db/all.fsa"
	run:
		if len(input) > 1:
			shell("cat {input} > {output}")
		else:
			shell("ln -sr {input} {output}")


rule combine_plasmidfinder_fsa:
	input:
		expand("/mnt/db/amr_annotation_db/plasmidfinder_db/{pfile}.fsa", pfile=plafiles)
	output:
		"output/plasmidfinder_db/all.fsa"
	run:
		if len(input) > 1:
			shell("cat {input} > {output}")
		else:
			shell("ln -sr {input} {output}")


# this rule follows a couple of command line steps in order to add the sequence length to the header of each appropriate sequence
rule add_seqLen:
	input:
		i1="output/resfinder_db/all.fsa",
		i2="output/plasmidfinder_db/all.fsa",
		i3="databases/nt_db/nt.2.fa"
		#hier dan mogelijk de eigen custom db in als i3? moet wel doorgerekend worden in de opeenvolgende rules
	output:
		o1="output/added_seqLen/resfinder.fsa",
		o2="output/added_seqLen/plasmidfinder.fsa",
		o3="output/added_seqLen/nt2.fsa" 
		#hier dan mogelijk de eigen custom db out als o3? moet wel doorgerekend worden in de opeenvolgende rules
	shell:
		"""cat {input.i1} | seqkit fx2tab --length | awk -F "\\t" '{{print $1"_"$4"\\t"$2}}' | seqkit tab2fx > {output.o1} | cat {input.i2} | seqkit fx2tab --length | awk -F "\\t" '{{print $1"_"$4"\\t"$2}}' | seqkit tab2fx > {output.o2} | cat {input.i3} | seqkit fx2tab --length | awk -F "\\t" '{{print $1"_"$4"\t"$2}}' | seqkit tab2fx > {output.o3}"""

# this was made for the inclusion of the ncbi nt database
# cat head27_nt2.fa | seqkit fx2tab --length | awk 'BEGIN {FS = "\\t" } ; {{print $1"_"$4"\t"$2}}' | seqkit tab2fx
		
# this rule utilizes the script resfinder_dbUpdate.py to create Genbank (.gb) formatted files from the FASTA (.fsa) input files.
# the Python script uses the sequence and different positions in the header to format the inforation into an Genbank file.
rule resfinder_gb:
	input:
		"output/added_seqLen/resfinder.fsa"
	output:
		"output/resfinder_gb/resfinder.gb"
	shell:
		"python scripts/resfinder_dbUpdate.py {input} > {output}"

# this rule utilizes the script plasmidfinder_dbUpdate.py to create Genbank (.gb) formatted files from the FASTA (.fsa) input files.
# initially the code works the same as it is partially a copy of resfinder_dbUpdate.py, but different codes were constructed because plasmidfinder was structured differently.
rule plasmidfinder_gb:
	input:
		"output/added_seqLen/plasmidfinder.fsa"
	output:
		"output/plasmidfinder_gb/plasmidfinder.gb"
	shell:
		"python scripts/plasmidfinder_dbUpdate.py {input} > {output}"
		
# this rule utilizes the script plasmidfinder_dbUpdate.py to create Genbank (.gb) formatted files from the FASTA (.fsa) input files.
# initially the code works the same as it is partially a copy of resfinder_dbUpdate.py, but different codes were constructed because plasmidfinder was structured differently.
rule nt_gb:
	input:
		"output/added_seqLen/nt2.fsa"
	output:
		"output/nt_gb/nt2.gb"
	benchmark:
		"output/benchmark/nt_gb.txt"
	shell:
		"python scripts/nt_dbUpdate.py {input} > {output}"

# this rule uses a short command to remove the first line of the file, this was used to prepare both files for eventual merge.
# this also tackles a problem occured that '//' was printed as the first line of the file.
rule remove_line1:
	input:
		i1="output/resfinder_gb/resfinder.gb",
		i2="output/plasmidfinder_gb/plasmidfinder.gb",
		i3="output/nt_gb/nt2.gb"
	output:
		o1="output/removed_line1/resfinder.gb",
		o2="output/removed_line1/plasmidfinder.gb",
		o3="output/removed_line1/nt2.gb"
	benchmark:
		"output/benchmark/remove_line1.txt"
	shell:
		"sed '1d' {input.i1} > {output.o1} | sed '1d' {input.i2} > {output.o2} | sed '1d' {input.i3} > {output.o3}"

# this rule uses two short commands to add '//' as the last line of the file, this to properly close the Genbank entries.
rule add_fSlash:
	input:
		i1="output/removed_line1/resfinder.gb",
		i2="output/removed_line1/plasmidfinder.gb",
		i3="output/removed_line1/nt2.gb"
	output:
		o1="output/reference/Resfinder_Reference_Genes.gb",
		o2="output/reference/Plasmidfinder_Reference_Genes.gb",
		o3="output/reference/NT_Reference_Genes.gb"
	benchmark:
		"output/benchmark/add_fSlash.txt"
	shell:
		"""echo "//" >> {input.i1} | mv {input.i1} {output.o1} | echo "//" >> {input.i2} | mv {input.i2} {output.o2} | echo "//" >> {input.i3} | mv {input.i3} {output.o3}"""

# this rule merges the two databases together and results in the complete reference database.
rule merge_output:
	input:
		"output/reference/Resfinder_Reference_Genes.gb",
		"output/reference/Plasmidfinder_Reference_Genes.gb",
		"output/reference/NT_Reference_Genes.gb"
	output:
		"output/reference/ResPlas_Reference_Genes.gb"
	run:
		if len(input) > 1:
			shell("cat {input} > {output}")
		else:
			shell("ln -sr {input} {output}")
