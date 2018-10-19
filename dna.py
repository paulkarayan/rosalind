
# Given: A DNA string s of length at most 1000 nt.
# Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.
import collections

## test cases
SAMPLE_DATASET = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
SAMPLE_OUTPUT = "0 12 17 21"


def main(dna_string):
    nucleotide_counter = collections.Counter(dna_string)

    print nucleotide_counter
    print nucleotide_counter["A"]
    # print "{A}".format(,
                                #    nucleotide_counter.get("C"),
                                #    nucleotide_counter.get("G"),
                                #    nucleotide_counter.get("T"),
                                   )

if __name__ == "__main__":
    main(SAMPLE_DATASET)