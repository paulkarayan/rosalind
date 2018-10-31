# Either strand of a DNA double helix can serve as the coding strand for RNA transcription. 
# Hence, a given DNA string implies six total reading frames, or ways in which the 
# same region of DNA can be translated into amino acids: 
# three reading frames result from reading the string itself, whereas three more 
# result from reading its reverse complement.

# Given: A DNA string s of length at most 1 kbp in FASTA format.
# Return: Every distinct candidate protein string that can be translated from ORFs of s. 
# Strings can be returned in any order.

## REMEMBER: M is the start codon

from utils import fasta_breakup
from utils import RNA_CODON_TABLE
from utils import reverse_complement
from utils import dna_to_rna


## test cases
SAMPLE_DATASET = """>Rosalind_99
AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG
"""
SAMPLE_OUTPUT = """MLLGSFRLIPKETLIQVAGSSPCNLS
M
MGMTPRLGLESLLE
MTPRLGLESLLE"""


def main(fasta_block):
    dna_dict = fasta_breakup(fasta_block)
    dna_target = dna_dict.values()[0]

    rna_target = dna_to_rna(dna_target)
    rev_comp_dna = "".join(reverse_complement(dna_target))
    rev_comp_rna = dna_to_rna(rev_comp_dna)

    protein_strings = []
    for start in find_all(rna_target, 'AUG'):
        protein_strings.append(translate(start, rna_target))
    
    for start in find_all(rev_comp_rna, 'AUG'):
        protein_strings.append(translate(start, rev_comp_rna))
    
    #dedupe and remove Nones
    protein_strings = [prot for prot in protein_strings if prot != None]
    cleaned_proteins = list(set(protein_strings))
    return "\n".join(cleaned_proteins)

    # translate(rna_target.find('AUG'), rna_target)

def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub) # use start += 1 to find overlapping matches

def translate(start_pos, rna_string):
    protein_string = ''
    for pos in range(start_pos, len(rna_string), 3):
        codon = rna_string[pos:pos+3]
        if RNA_CODON_TABLE[codon] == 'stop':
            return protein_string
        protein_string += RNA_CODON_TABLE[codon]
    return


if __name__ == "__main__":
    ## Test
    # main(SAMPLE_DATASET)
    assert main(SAMPLE_DATASET) == SAMPLE_OUTPUT

    ## Prod
    with open("./datasets/rosalind_orf.txt", 'r') as fptr:
        fasta_block = fptr.read().strip()
        print main(fasta_block)