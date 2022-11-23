#!/usr/bin/env python3
import argparse

function='Takes a mixed sequence input file and sorts out sequences belonging to each chromosome in a separate file'

parser=argparse.ArgumentParser(description=function)
parser.add_argument('-v','--version',action='version',version='%(prog)s 1.0')
parser.add_argument('-i',metavar='INPUT_FASTA',help='input fastq file containing mixed sequences',dest='fastaIn',required=True)
args=parser.parse_args()

# Making a dictionary with sequence info as key and values
# Making a list to keep names of the present chromosomes
with open(args.fastaIn,'r') as fin:
    infoDict={}; chrList=[]
    for line in fin:
        if line.startswith('>'):
            id=line.split('\t')[0].lstrip('>'); chr=line.split('\t')[1]; strand=line.split('\t')[2].rstrip('\n'); seq=next(fin).rstrip('\n')
            infoDict[id]=chr,strand,seq
            if chr not in chrList:
                chrList.append(chr)
# Creating separate files for each chromosome and printing corresponding sequences into them
for i in chrList:
    with open(i+'.fna','w') as fout:
        for j in infoDict:
            if infoDict[j][0]==i:
                print('>'+j,'\t',infoDict[j][0],'\t',infoDict[j][1],'\n',infoDict[j][2],file=fout)
