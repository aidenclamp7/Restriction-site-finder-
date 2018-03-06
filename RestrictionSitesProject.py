from Bio import Entrez
from Bio import SeqIO
import sys
import argparse

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
    print("\nID: {}, \nDescription: {}, \nDNA Sequence: \n{}\n".format(a[0], a[1],
                                                                insert_newlines(str(a[2]))))
def insert_newlines(string, every=80):
    lines = []
    for i in range(0, len(string), every):
        lines.append(string[i:i+every])
    return '\n'.join(lines)

def findRS(x):
    a = accessncbi(x)
    lst = []
    for i in RSlist:
        if i not in str(a[2]):
            pass
        else:
            lst.append(i)
    print('\n'.join('{}:{}'.format(*k) for k in enumerate(lst, 1)))

parser = argparse.ArgumentParser(description='Process some integer.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default:findthe max')

args = parser.parse_args()
print(args.accumulate(args.integers))

def masterfunction(x):
    findseq(x)
    findRS(x)



#masterfunction("EU490707")
#masterfunction("LZ221631")
#masterfunction("NM_057750")