from Bio import Entrez
from Bio import SeqIO

def accessncbi(x):
    Entrez.email = "aidenclamp@gmail.com"  # Need to tell NCBI your email address
    handle = Entrez.efetch(db="nucleotide", id=x, rettype="gb", retmode="text")
    record = SeqIO.read(handle, "genbank")
    handle.close()
    return record.id, record.description, record.seq

def insert_newlines(string, every=100):
    lines = []
    for i in range(0, len(string), every):
        lines.append(string[i:i+every])
    return '\n'.join(lines)

def findseq(x):
    print("ID {}, \nDescription {}, \nDNA Sequence \n{}".format(accessncbi(record.id, record.description, record.seq)))

findseq(accessncbi("EU490707"))