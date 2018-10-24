# The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or 'G'. 
# For example, the GC-content of "AGCTATAG" is 37.5%. Note that the reverse complement of any DNA string has the same GC-content.
# DNA strings must be labeled when they are consolidated into a database. A commonly used method of string labeling is called FASTA format. 
# In this format, the string is introduced by a line that begins with '>', followed by some labeling information. 
# Subsequent lines contain the string itself; the first line to begin with '>' indicates the label of the next string.
# In Rosalind's implementation, a string in FASTA format will be labeled by the ID "Rosalind_xxxx", where "xxxx" denotes 
# a four-digit code between 0000 and 9999.

# Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
# Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. 
# Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.

import collections
import operator

from utils import chunks


## test cases
SAMPLE_DATASET = """>Rosalind_6404
                    CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
                    TCCCACTAATAATTCTGAGG
                    >Rosalind_5959
                    CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
                    ATATCCATTTGTCAGCAGACACGC
                    >Rosalind_0808
                    CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
                    TGGGAACCTGCGGGCAGTAGGTGGAAT"""

SAMPLE_OUTPUT = """Rosalind_0808
                   60.919540"""


def main(fasta_block):
    fasta_dict = fasta_breakup(fasta_block)

    max_dict = {}
    for label, bases in fasta_dict.items():
        # print gc_content(bases) * 100
        max_dict[label] = gc_content(bases) * 100
    # get max
    max_gc_label = max(max_dict.iteritems(), key=operator.itemgetter(1))[0]
    # print max_gc_label + "\n" + '%.6f' % max_dict[max_gc_label]
    return max_gc_label + "\n" + '%.6f' % max_dict[max_gc_label]

def gc_content(dna_string):
    gc_count = collections.Counter(dna_string)
    # print dict(gc_count)
    # maybe refactor into two funcs - for now, get gc %
    return float(gc_count['C'] + gc_count['G']) / len(dna_string)


def fasta_breakup(fasta_block):
    fasta_strings = fasta_block.split(">")
    # remove empty strings, such as when you newline by accident
    fasta_strings = filter(None, fasta_strings)
    #strip whitespaces
    # fasta_strings = [str_.strip() for str_ in fasta_strings]
    fasta_strings = ["".join(str_.split(" ")) for str_ in fasta_strings]

    fasta_dict = {}

    for subunit in fasta_strings:
        fasta_label = subunit.split("\n")[0]
        bases = ''.join(subunit.split("\n")[1:])
        fasta_dict[fasta_label] = bases

    return fasta_dict


if __name__ == "__main__":
    ## Test
    # print main(SAMPLE_DATASET)
    result = SAMPLE_OUTPUT.replace(" ", "")
    assert main(SAMPLE_DATASET) == result

    ## Prod
    with open("./datasets/rosalind_gc.txt", 'r') as fptr:
       dna = fptr.read()
       print dna
       print main(dna)