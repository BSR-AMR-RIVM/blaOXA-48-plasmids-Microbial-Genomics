# import command line interpretation
import sys
# import of wildcards and directory functions
import glob, os

# This method of constructing the configuration file was chosen to uphold Snakemake's flow while dynamically changing its input.
# !! when using new files please utilize python makeconfig.py > config.yaml, this to ensure run with the new files!!

print("run:")
d = "input"
for file in os.listdir(d):
    # splitext(file)[0] gives the filename without extension
    if file.endswith(".fasta"):
            config = " " + os.path.splitext(file)[0] + ": " + d + "/" + file
            print(config)
    elif file.endswith(".fa"):
            config = " " + os.path.splitext(file)[0] + ": " + d + "/" + file
            print(config)
    elif file.endswith(".fna"):
            config = " " + os.path.splitext(file)[0] + ": " + d + "/" + file
            print(config)
    elif file.endswith(".fsa"):
            config = " " + os.path.splitext(file)[0] + ": " + d + "/" + file
            print(config)
