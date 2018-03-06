from Bio import Entrez
from Bio import SeqIO

RSlist = ["AAA","TTTT","CCCC","GGGG","AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"]

def accessncbi(x):
    Entrez.email = "aidenclamp@gmail.com"  # Need to tell NCBI your email address
    handle = Entrez.efetch(db="nucleotide", id=x, rettype="gb", retmode="text")
    record = SeqIO.read(handle, "genbank")
    handle.close()
    return record.id, record.description, record.seq

def findseq(x):
    a = accessncbi(x)
    print("ID: {}, \nDescription: {}, \nDNA Sequence: \n{}".format(a[0], a[1],
                                                                insert_newlines(str(a[2]))))
def insert_newlines(string, every=100):
    lines = []
    for i in range(0, len(string), every):
        lines.append(string[i:i+every])
    return '\n'.join(lines)

def findRS(x):
    a = accessncbi(x)
    for i in RSlist:
        if i not in str(a[2]):
            return print("True")
        else:
            return print("False")

def masterfunction(x):
    findseq(x)
    findRS(x)

masterfunction("EU490707")