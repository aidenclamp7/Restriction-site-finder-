from Bio import Entrez
from Bio import SeqIO

RSlist = ["GAATTC","GGATCC","AAGCTT","TCGA","GCGGCCGC", "GANTC",
          "GATC", "CAGCTG" , "CCCGGG", "GGCC", "GACGC", "AGCT",
          "GATATC", "GGTACC","CTGCAG", "GAGCTC", "GTCGAC","AGYACT",
          "ACTACT","ACTAGT","GCATGC","AGGCCT","TCTAGA"]

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
    lst = []
    for i in RSlist:
        if i not in str(a[2]):
            lst.append("Not Found")
        else:
            lst.append("Found")
    print('\n'.join('{}:{}'.format(*k) for k in enumerate(lst, 1)))

def masterfunction(x):
    findseq(x)
    findRS(x)

masterfunction("EU490707")