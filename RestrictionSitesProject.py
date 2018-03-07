from Bio import Entrez
from Bio import SeqIO
import argparse

RSlist = ["GAATTC","GGATCC","AAGCTT","TCGA","GCGGCCGC", "GANTC",
          "GATC", "CAGCTG" , "CCCGGG", "GGCC", "GACGC", "AGCT",
          "GATATC", "GGTACC","CTGCAG", "GAGCTC", "GTCGAC","AGYACT",
          "ACTACT","ACTAGT","GCATGC","AGGCCT","TCTAGA"]

def accessncbi(x,y):
    Entrez.email = y  # Need to tell NCBI your email address
    handle = Entrez.efetch(db="nucleotide", id=x, rettype="gb", retmode="text")
    record = SeqIO.read(handle, "genbank")
    handle.close()
    return record.id, record.description, record.seq

def findseq(x,y):
    a = accessncbi(x,y)
    print("\nID: {}, \nDescription: {}, \nDNA Sequence: \n{}\n".format(a[0], a[1],
                                                                insert_newlines(str(a[2]))))
def insert_newlines(string, every=80):
    lines = []
    for i in range(0, len(string), every):
        lines.append(string[i:i+every])
    return '\n'.join(lines)

def findRS(x,y):
    a = accessncbi(x,y)
    lst = []
    for i in RSlist:
        if i not in str(a[2]):
            pass
        else:
            lst.append(i)
    print('\n'.join('{}:{}'.format(*k) for k in enumerate(lst, 1)))

parser = argparse.ArgumentParser(description='A program that can find Restriction Sites in a DNA sequence.')
parser.add_argument('NCBI_ID_number', type=str, action="store",
                    help='This is an NCBI ID number. A valid NCBI number has two letters'
                         ' followed by six numbers e.g. EU490707')
parser.add_argument('Email_Adress', type=str, action="store",
                    help="NCBI requres an email adress to access the database")

args = parser.parse_args()

def test1(x,y):
    if len(x)==8:
        return True
    else:
        return False, print("Please use a valid NCBI ID number.")
def test2(x,y):
    if "@" in y:
        return True
    else:
        return False, print("Please use a valid email adress")
def test3(x,y):
    if "." in y:
        return True
    else:
        return False, print("Please use a valid email adress")
def test4(x,y):
    if y.find("@") < y.find("."):
        return True
    else:
        return False, print("Please use a valid email adress")
def test5(x,y):
    if " " in y:
        return True
    else:
        return False, print("Please use a valid email adress")

def masterfunction(x,y):
    b = test1(x,y)
    c = test2(x,y)
    d = test3(x,y)
    e = test4(x,y)
    f = test5(x,y)
    if b == True:
        pass
    if c == True:
        pass
    if d == True:
        pass
    if e == True:
        pass
    if f == True:
        pass
    else:
        return print("Use the --help command for details")
    findseq(x,y)
    findRS(x,y)

masterfunction(args.NCBI_ID_number, args.Email_Adress)
#masterfunction("EU490707")
#masterfunction("LZ221631")
