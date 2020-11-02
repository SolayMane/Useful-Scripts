# Useful scripts
## This script aims to donwload complete genome sequence for a given species from bacteria
### we will download all genome summaries from bacteria fungi and virus
```bash
for genus in viral bacteria fungi
do
  curl https://ftp.ncbi.nlm.nih.gov/genomes/refseq/$genus/assembly.summary.txt -o $genus.assembly.summary.txt


#retrieve the ftp paths for complete genome from assembly summary files

awk -F '\t' ' ($12 == "Complete Genome") && ($11 == "latest") {print $20}' ${genus}.assembly.summary.txt > ${genus}.ftpdirpaths.txt

#using the ftp path, donwload the genomes and save them to kingdome folder already created.
        cat ${genus}.ftpdirpaths.txt | while read line
        do

#downlonding the genomes, you can donwload proteins changing the file extention to _protein.faa.gz
                curl https://ftp.ncbi.nlm.nih.gov/genomes/refseq/$genus/${line##*genomes/}/${line##*/}_genomic.fna.gz -o data_fna/$genus/${line##*/}_genomic.fna.gz
        done
done
````
