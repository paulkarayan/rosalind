
# Given: A DNA string s of length at most 1000 nt.
# Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.
import collections

## test cases
SAMPLE_DATASET = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
SAMPLE_OUTPUT = "20 12 17 21"


def main(dna_string):
    nucleotide_counter = collections.Counter(dna_string)

    print "{A} {C} {G} {T}".format(A=nucleotide_counter["A"],
                                   C=nucleotide_counter["C"],
                                   G=nucleotide_counter["G"],
                                   T=nucleotide_counter["T"],
                                  )

if __name__ == "__main__":
    # main(SAMPLE_DATASET)
    with open("./datasets/rosalind_dna.txt", 'r') as fptr:
        dna = fptr.read()
        main(dna) 
