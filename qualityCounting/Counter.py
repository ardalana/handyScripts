#!/usr/bin/env python3
import sys

# Program to count the number of certain bases with certain quality value in a given fastq file (e.g. SRR1614671)
base=sys.argv[1].upper()
qual=sys.argv[2]
readsFile=sys.argv[3]

seqs=[];scors=[]
count=0

with open(readsFile) as infile:
    for line in infile:
        if line.startswith('@SRR1614671'):
            seqs.append(next(infile))
        if line.startswith('+SRR1614671'):
            scors.append(next(infile))
for i in range(len(seqs)):
    for j in range(len(seqs[i])):
        if seqs[i][j]==base and scors[i][j]==qual:
            count+=1
print(count)
