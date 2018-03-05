from Bio import Entrez
from Bio import SeqIO
Entrez.email = "aidenclamp@gmail.com" # Need to tell NCBI your email address
handle = Entrez.efetch(db="nucleotide", id="EU490707", rettype="gb", retmode="text")
record = SeqIO.read(handle, "genbank")
handle.close()

print(record.id)
print(record.description)
def insert_newlines(string, every=64):
    lines = []
    for i in range(0, len(string), every):
        lines.append(string[i:i+every])
    return '\n'.join(lines)

print(insert_newlines(str(record.seq)))

def accessncbi(x):
    Entrez.email = "aidenclamp@gmail.com"  # Need to tell NCBI your email address
    handle = Entrez.efetch(db="nucleotide", id=x, rettype="gb", retmode="text")
    record = SeqIO.read(handle, "genbank")
    handle.close()
    return print("ID {}, \nDescription {}, \nSequence {}".format(record.id, record.description, insert_newlines(str(record.seq))))

accessncbi("EU490707")