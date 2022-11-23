#!/usr/bin/python3
# This program considers circular shape of mtDNA and generates, as well, read that bridge between end and beginning of the given linear genome. The input file contains sequence in one line.
import sys
import random

seqDep=int(input('Enter desired sequencing depth(x): '))
readLen=int(input('Enter desired read length(b): '))
dataFile=sys.argv[1]
readList=[]
readDict={}

with open(dataFile) as infile, open(dataFile+'.pseudoreads.circ','w') as outfile:
    for line in infile:
        if not line.startswith('>'):
            line=line.strip(); numReads=int(len(line)*seqDep/readLen)
            while len(readList)<=numReads:
                start=random.randrange(len(line)); residue=len(line)-start
                if residue<readLen:
                    readList.append(line[start:]+line[:readLen-residue])
                else:
                    readList.append(line[start:(start+readLen)])

    # for i in range(len(readList)):
    #     readDict['>pseudoread'+str(i)]=readList[i]

    for i in range(len(readList)):
        idDigits=len(str(i)); maxIdDigits=len(str(numReads)); reqZeros=maxIdDigits-idDigits
        readDict['>pseudoread'+'0'*reqZeros+str(i)]=readList[i]

    for j in readDict:
        print(j,readDict[j],sep="\n",file=outfile)
    #
    # Alternatively for having even read numbering to enable read sorting, as long as numReads is 4 digits:
    #
    # for i in range(0,len(readList)):
    #     readID='>pseudoread'+str(i)
    #     if len(readID)<15:
    #         zeros=15-len(readID)
    #         if zeros==3:
    #             readDict['>pseudoread000'+str(i)]=readList[i]
    #         if zeros==2:
    #             readDict['>pseudoread00'+str(i)]=readList[i]
    #         if zeros==1:
    #             readDict['>pseudoread0'+str(i)]=readList[i]
    #     else:
    #         readDict['>pseudoread'+str(i)]=readList[i]
    #
    # for j in sorted(readDict):
    #     print(j,readDict[j],sep="\n",file=outfile)
