# Given: A DNA string s (of length at most 1 kbp) and a collection of substrings of 
# s acting as introns. All strings are given in FASTA format.
# Return: A protein string resulting from transcribing and translating the exons of s. 
# (Note: Only one solution will exist for the dataset provided.)

from utils import fasta_breakup
from utils import dna_to_rna
from utils import translate_rna_to_protein


## test cases
SAMPLE_DATASET = """>Rosalind_10
ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG
>Rosalind_12
ATCGGTCGAA
>Rosalind_15
ATCGGTCGAGCGTGT"""
SAMPLE_OUTPUT = "MVYIADKQHVASREAYGHMFKVCA"


def main(fasta_block):
    dna_dict = fasta_breakup(fasta_block)
    
    #get largest one - rest will be introns
    largest_dna = max(dna_dict.values(), key=len)
    introns = dna_dict.values()
    introns.remove(largest_dna)
    
    for intron in introns:
        largest_dna = largest_dna.replace(intron, "")

    rna_target = dna_to_rna(largest_dna)
    return translate_rna_to_protein(rna_target)


if __name__ == "__main__":
    ## Test
    # main(SAMPLE_DATASET)
    assert main(SAMPLE_DATASET) == SAMPLE_OUTPUT

    ## Prod
    with open("./datasets/rosalind_splc.txt", 'r') as fptr:
        fasta_block = fptr.read().strip()
        print main(fasta_block)