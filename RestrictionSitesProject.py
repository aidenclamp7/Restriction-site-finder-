from Bio import Entrez
from Bio import SeqIO

def accessncbi(x):
    Entrez.email = "aidenclamp@gmail.com"  # Need to tell NCBI your email address
    handle = Entrez.efetch(db="nucleotide", id=x, rettype="gb", retmode="text")
    record = SeqIO.read(handle, "genbank")
    handle.close()
    return record.seq, print("ID {}, \nDescription {}, \nDNA Sequence \n{}".format(record.id, record.description,
                                                                                   insert_newlines(str(record.seq))))


def insert_newlines(string, every=100):
    lines = []
    for i in range(0, len(string), every):
        lines.append(string[i:i+every])
    return '\n'.join(lines)


def findRS(x):
    a = accessncbi(x)
    if "A" not in str(a[0]):
        return print("True")
    else:
        print("False")

findRS("EU490707")

RSlist = ["AAA","TTTT","CCCC","GGGG"]
print(RSlist)

