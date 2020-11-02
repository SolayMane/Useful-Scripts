# Hello-world
# This script aims to donwload complete genome sequence for a given species from bacteria

## step one
### we will download all summries from bacteria fungi and viral
```bash
for genus in viral bacteria fungi
do
  wget https://ftp.ncbi.nlm.nih.gov/genomes/refseq/bacteria/assembly.summary.txt
done
```
