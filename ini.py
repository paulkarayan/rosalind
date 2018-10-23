# use biopython! that requires python3 for mac osx apparently
# python3 /Users/pkarayan/rosalind/ini.py

# One of the simplest SMS 2 programs, called DNA stats, counts the number of occurrences 
# of each nucleotide in a given strand of DNA.

# Given: A DNA string s of length at most 1000 bp.
# Return: Four integers (separated by spaces) representing the respective number of times that the symbols 
# 'A', 'C', 'G', and 'T' occur in s. Note: You must provide your answer in the format shown in the sample output below.

from Bio.Seq import Seq
# >>> my_seq = Seq("AGTACACTGGT")
# >>> my_seq.count("A")


## test cases
SAMPLE_DATASET = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
SAMPLE_OUTPUT = "20 12 17 21"


def main(dna_sequence):
    sequence = Seq(dna_sequence)

    return "{A} {C} {G} {T}".format(A=sequence.count("A"),
                                   C=sequence.count("C"),
                                   G=sequence.count("G"),
                                   T=sequence.count("T")
    )


if __name__ == "__main__":
    ## Test
    # print(main(SAMPLE_DATASET))
    # assert main(SAMPLE_DATASET) == SAMPLE_OUTPUT

    ## Prod
    with open("./datasets/rosalind_ini.txt", 'r') as fptr:
       dna = fptr.read().strip()
       print(main(dna))