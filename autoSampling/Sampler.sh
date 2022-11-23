randSeed=50
seedLeap=250
sampleSize=50000
sizeLeap=250000
ls *_1.fastq | while read line; do
if sampleSize<=6800000; then
seqtk sample -s$randSeed $line $sampleSize > $line.sub1
randSeed+=seedLeap
sampleSize+=sizeLeap
fi
done
