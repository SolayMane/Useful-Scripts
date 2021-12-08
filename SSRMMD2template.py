import pandas as pd
import numpy as np
from collections import Counter

from pandas.tseries import frequencies

path = r"F:/Arganier/SSRs/SSRMMD/SSR_motif_stat.xlsx"

# retrive the template co,ntaing the ssr (flanking sequences)
flanking_seqs = open("F:/Arganier/SSRs/SSRMMD/SSR_template.fasta","w")

with open("F:/Arganier/SSRs/SSRMMD/ArganiaSpinosa.fa.SSRs", "r") as f:
    next(f) #skip the first line containing the headers
    
    patterns = []   
    repeat_count = []
    ssrMotifs = []
    
    for line in f:
        
        motif = line.split("\t")[2]
        lseq = line.split("\t")[8]
        rseq = line.split("\t")[10]
        repeat = line.split("\t")[4]
        motif_length = line.split("\t")[3]
        header = ">" + line.split("\t")[0] + "_" + line.split("\t")[1]
        template = header +"\n"+lseq + int(repeat)*motif + rseq # write the template into the fasta file
        repeat_size = line.split("\t")[5]
        patterns.append(motif)
        repeat_count.append(repeat_size)
        ssrMotifs.append(motif_length)
        flanking_seqs.write(template+"\n")
    motif_stat= Counter(patterns)# this is to count for each ssr motif the number of repeats
    repeat_occurrence = Counter(repeat_count)
    ssrpat = Counter(ssrMotifs)
writer = pd.ExcelWriter(path, engine = 'xlsxwriter')

# creat a table ( data frame) with infromation for evrey ssr motif. 
df1=pd.DataFrame({"Motif" : motif_stat.keys(), "Occurrence" : motif_stat.values()})

df2=pd.DataFrame({"Repeat Length" : repeat_occurrence.keys(), "Occurrence" : repeat_occurrence.values()})

df3=pd.DataFrame({"Mers" : ssrpat.keys(), "Total Occurrence" : ssrpat.values()})

df1.to_excel(writer, index=False, sheet_name="Motif Occurrence")
df2.to_excel(writer, index=False, sheet_name="Repeat length occurrence")  
df3.to_excel("SSR_mot_dist.xlsx", index=False, sheet_name="SSR motif distribution")  
writer.save()
writer.close()
