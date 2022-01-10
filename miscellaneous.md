````bash


# to find files with specific extension in different directories and then copy them to a targeted directory
sudo find trg-1/ -type f -name "*.fastq.gz" -exec cp {} raw_data/ \; 

#to find empty file and delet them
find . -type f -size 0 -delete


#these commands are daily used for file precessing


#rename 's/M\-/M/' *.fastq # I want to remove a "-" from the names of multiples fastq files
#we can do  by using the sed command to replace things inside the fastq files :
sed 's/\-//g' *.fastq



#rename folders byy substring names 
ls | while read dir
do
	mv "$dir" "${dir##* }"
done


#copy a selected sequence fasta from folder to another based on their names
#ids.txt file containing the liste of sequence to copy
#/data/ folder containing the raw sequence /selected/ folder in which we will copy the wanted sequences
cat ids.txt | while read ids
do
 cp /data/${ids}.fa selected/
done

# to check disk usage topten bigger folder
du -a /home | sort -n -r | head -n 10


#tips to modify the header of fasta sequences file example Dso_IPO2222.faa
#example of header : >fig|1225786.7.peg.1 we want to convert it to Dickeya_solani_IPO2222.0001


cat Dso_IPO2222.faa | awk -v chaine="000" ' /^>/ {print ">Dickeya_solani_IPO2222."substr(chaine,1,23-length($1))substr($1,20,length($1)-19)} /[^>]/ {print $0}' | sed '/>fig/d' >  Dso_IPO2222.fast



#To add the tab-separated field names Runs, Opposition and Date, I can use any of the following commands:

echo -e "Runs\tOpposition\tDate" | cat - table > table_with_header
sed '1i Runs\tOpposition\tDate' table > table_with_header
awk 'BEGIN {print "Runs\tOpposition\tDate"} {print}' table > table_with_header



#split multifasta file into separate file sequence : It reads like this: 
#if the line starts with >, open a new file and write to it until you reach a new 
#line starting with >. Note it is not necessary to use >> with Awk (the output file is only opened once).

awk -F">" '/^>/ {F = $2".fasta"} { print > F}' 6cp.fasta


#### tip to rename long fasta headers to short using cat awk and while loop
 ls *.fa | while read file; do cat $file | awk -F"," '/^>/ { print "ZZZZ"$1 } /[^>]/ { print $0}' | sed '/^>/d' | sed 's/ZZZZ//g' > essai/$file; done


 ##### rename multifatsa file with incrementing headers :
 awk '/>/{print substr($0,1,1)"Contig"(++i)}!/>/' final.genome.scf.fasta >F.oxysporum_Foa113.fasta


#### fastq to fasta

######this code is aiming to columne 0 that existe in karyotype.test by col 1 from the file corr_scaf.txt
while IFS=, read -a line; do sed -i 's/'${line[0]}'/'${line[1]}'/g' karyotype.test ;done < corr_scaf.txt


#### in the file SRR13198489_1.fastq,  {find a line starting with string (here +) and remove all strings afterit (here we have a word starting with SRR)
sed -i '/^+/ s/SRR.*//' SRR13198489_1.fastq




#### ustilser awk pour recuperer des lignes en se bsastn sur un pattern et aussi recupperer la ligne qui suive le pattern (exemeplt de resulta de blast enligne de fichier multi fasta)
cat ZAWWXRSX01R-Alignment.txt | awk -F" " -v n=1 ' /^Query #/ {printf $3"\t"$7"\t"$8"\t"} /^Description/ {f[NR+n]} NR in f' > resulFormated.txt


### error with dpkg 


Essentially:
Add exit 0 after the shebang to /var/lib/dpkg/info/snapd.prerm. Then run the following commands.

dpkg --purge --force-all snapd
apt-get update
Optionally re-install by running apt-get install snapd

````
