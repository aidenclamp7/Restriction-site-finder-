from Bio import Entrez
from Bio import SeqIO
import argparse

# RSlist is a list of example restriction sites that will be checked in the DNA sequence.
# More restriction sites can be added to the list to make the program more efective
RSlist = ["GAATTC","GGATCC","AAGCTT","TCGA","GCGGCCGC", "GANTC",
          "GATC", "CAGCTG" , "CCCGGG", "GGCC", "GACGC", "AGCT",
          "GATATC", "GGTACC","CTGCAG", "GAGCTC", "GTCGAC","AGYACT",
          "ACTACT","ACTAGT","GCATGC","AGGCCT","TCTAGA"]

# accessncbi if a function that uses an id number(x) and an email adress(y) to access the NCBI database
# The function will return a sequence records id, description and DNA sequence
# This function was made with help from the Biopython documentation
def accessncbi(x,y):
    Entrez.email = y  # y is where the email adress is used because you need to tell NCBI your email address
    handle = Entrez.efetch(db="nucleotide", id=x, rettype="gb", retmode="text") # x is where the NCBI ID is used
    record = SeqIO.read(handle, "genbank")
    handle.close()
    return record.id, record.description, record.seq

# findseq is a function that uses the returned id, description and sequence from accessncbi and formats it
# This will appear at the start of the output to show the id, description and sequence that the program is using
def findseq(x,y):
    a = accessncbi(x,y)
    print("\nID: {}, \nDescription: {}, \nDNA Sequence: \n{}\n".format(a[0], a[1],
                                                                insert_newlines(str(a[2]))))
# insert_newlines is a function that add new lines tom long strings.
# It is used for the DNA sequences because they are very often very long and go of the side of the screen
# Using this function makes them more readable
# This function was made with help from information of Stackoverflow
def insert_newlines(string, every=80):
    lines = []
    for i in range(0, len(string), every):
        lines.append(string[i:i+every])
    return '\n'.join(lines)

# findRS is a function that searches through a DNA sequence to find the restriction sites from RSlist
def findRS(x,y):
    a = accessncbi(x,y)
    lst = [] # This creates an empty list for the found RS to be stored in
    for i in RSlist:
        if i not in str(a[2]): #if the RS is not found it will just pass so it is not added to the list
            pass
        else:
            lst.append(i) # This adds found RS to the list
    print('\n'.join('{}:{}'.format(*k) for k in enumerate(lst, 1))) # This formats and numbers then list of found RS

# The next few lines create a parser and aguments so that the program ca be run of the terminal
# It has a description to say what the program does
# There are two arguments for the program.
# The two arguments form the inputs for most of the functions in the program
# The first argument is the NCBI ID number.This isn stored as a string because accessncbi requires a string
# The second argument is an email address because NCBI needs an email address.
# This is also stored as a string because accessncbi needs a string
# This was made with help from the python 3 documentation
parser = argparse.ArgumentParser(description='A program that can find Restriction Sites in a DNA sequence.')
parser.add_argument('NCBI_ID_number', type=str, action="store",
                    help='This is an NCBI ID number. A valid NCBI number has two letters'
                         ' followed by six numbers e.g. EU490707')
parser.add_argument('Email_Adress', type=str, action="store",
                    help="NCBI requres an email adress to access the database")

args = parser.parse_args()

# The following few functions are tests to ensure that the user has imputed the arguments correctly
# This is done because it is easy to break the code of the user inputs something the program does not expect
# both arguments are given to each test but only one is used this is because the program will give two arguments and
# will produce an error if the test is only expecting one.

def test1(x,y):
    if len(x)==8: # This ensures that the ID is the correct length
        return True
    else:
        return False

def test2(x,y):
    if "@" in y: # This ensures the email has an @ in it
        return True
    else:
        return False

def test3(x,y):
    if "." in y: # This ensures the email has a . in it
        return True
    else:
        return False

def test4(x,y): # This ensures the @ is before the .
    if y.find("@") < y.find("."):
        return True
    else:
        return False

def test5(x,y): # This ensures that there isnt a space in the email.
    if " " not in y:
        return True
    else:
        return False

# This the masterfunction. This function takes the arguments from the user and inputs them into the other functions.
# It also says what order the functions need to be done in.
# The tests are run first
# This ensures that only correct arguments will run
# If a test fails it will use exit() to stop the script
# If an argument was inputed incorrectly it would produce a large error message that someone who is unfamiliar
# with programming might find intimidating.
# So before exiting it will produce a simpler error message say exactly what the problem is
# After the testing it will run findseq followed by findRS.
# This is so the id, description and sequence is given before the found RS in the output
def masterfunction(x,y):
    b = test1(x,y)
    c = test2(x,y)
    d = test3(x,y)
    e = test4(x,y)
    f = test5(x,y)
    if b == True:
        pass
    else:
        print("Please use a valid NCBI ID number \nUse the --help command for details")
        exit()
    if c == True:
        pass
    else:
        print("Please use a valid email adress \nUse the --help command for details")
        exit()
    if d == True:
        pass
    else:
        print("Please use a valid email adress \nUse the --help command for details")
        exit()
    if e == True:
        pass
    else:
        print("Please use a valid email adress \nUse the --help command for details")
        exit()
    if f == True:
        pass
    else:
        print("Please use a valid email adress \nUse the --help command for details")
        exit()

    findseq(x,y)
    findRS(x,y)

# This the function actually being used with parser arguments as the inputs
masterfunction(args.NCBI_ID_number, args.Email_Adress)

# This is some example data if the user wishes to run the scrip in the python editor instead of the terminal
#masterfunction("EU490707", "example@email.com")
#masterfunction("LZ221631", "example@email.com")
