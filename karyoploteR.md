## How to plot your custom genome from fasta file:
````R
library(karyoploteR)
library(GenomicRanges)
library(seqinr)


# read the genome file
seqs <- readDNAStringSet("mygenome.fasta")

# show the names of the chromosomes :
names(seqs)
# show the length of every chromosome
width(seqs)
# so we will use theses data to build a custom genome for our sequence using toGranges

custom.genome <- toGRanges(data.frame(chr=c(names(seqs)), start=c(1), end=c(width(seqs)))

# then we will plot the chromosome
 kp <- plotKaryotype(genome=custom.genome)
 ````
