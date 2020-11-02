# Useful scripts
## This script aims to donwload complete genome sequence for a given species from bacteria
### we will download all summries from bacteria fungi and viral
```bash
for genus in viral bacteria fungi
do
  wget https://ftp.ncbi.nlm.nih.gov/genomes/refseq/$genus/assembly.summary.txt


#retrieve the ftp paths for complete genome from assembly summary files

awk -F '\t' ' ($12 == "Complete Genome") && ($11 == "latest") {print $20}' ${genus}.assembly_summary.txt > ${genus}.ftpdirpaths.txt

#using the ftp path, donwload the genomes and save them to kingdome folder already created.
        cat ${genus}.ftpdirpaths.txt | while read line
        do

#downlonding is performed using aspera software
                curl https://ftp.ncbi.nlm.nih.gov/genomes/refseq/$genus/${line##*genomes/}/${line##*/}_genomic.fna.gz -o data_fna/$genus/${line##*/}_genomic.fna.gz
        done
done
````
