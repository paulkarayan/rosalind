#  transition to transversion ratio
from __future__ import division

from utils import fasta_breakup

## test cases
SAMPLE_DATASET = """>Rosalind_0209
GCAACGCACAACGAAAACCCTTAGGGACTGGATTATTTCGTGATCGTTGTAGTTATTGGA
AGTACGGGCATCAACCCAGTT
>Rosalind_2200
TTATCTGACAAAGAAAGCCGTCAACGGCTGGATAATTTCGCGATCGTGCTGGTTACTGGC
GGTACGAGTGTTCCTTTGGGT"""
SAMPLE_OUTPUT = "1.21428571429"

TRANSITION = [('A', 'G'), ('G', 'A'), ('C','T'), ('T', 'C')]


def main(fasta_block):
    dna_dict = fasta_breakup(fasta_block)

    dna_one, dna_two = dna_dict.values()
    # print dna_one, dna_two
    transition_count, transversion_count = 0, 0 
    assert len(dna_one) == len(dna_two) 
    for idx, base in enumerate(dna_one):
        if (base, dna_two[idx]) in TRANSITION:
            transition_count += 1
        elif base != dna_two[idx]:
            transversion_count += 1

    # print transversion_count, transition_count
    return transition_count / transversion_count


if __name__ == "__main__":
    ## Test
    # print main(SAMPLE_DATASET)
    # assert main(SAMPLE_DATASET) == SAMPLE_OUTPUT

    ## Prod
    with open("./datasets/rosalind_tran.txt", 'r') as fptr:
        fasta_block = fptr.read().strip()
        print main(fasta_block)