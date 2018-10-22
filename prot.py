# Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).
# Return: The protein string encoded by s.

from utils import chunks

## test cases
SAMPLE_DATASET = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
SAMPLE_OUTPUT = "MAMAPRTEINSTRING"


RNA_CODON_TABLE = {
    'UUU': 'F',     'CUU': 'L',     'AUU': 'I',     'GUU': 'V',
    'UUC': 'F',     'CUC': 'L',     'AUC': 'I',     'GUC': 'V',
    'UUA': 'L',     'CUA': 'L',     'AUA': 'I',     'GUA': 'V',
    'UUG': 'L',     'CUG': 'L',     'AUG': 'M',     'GUG': 'V',
    'UCU': 'S',     'CCU': 'P',     'ACU': 'T',     'GCU': 'A',
    'UCC': 'S',     'CCC': 'P',     'ACC': 'T',     'GCC': 'A',
    'UCA': 'S',     'CCA': 'P',     'ACA': 'T',     'GCA': 'A',
    'UCG': 'S',     'CCG': 'P',     'ACG': 'T',     'GCG': 'A',
    'UAU': 'Y',     'CAU': 'H',     'AAU': 'N',     'GAU': 'D',
    'UAC': 'Y',     'CAC': 'H',     'AAC': 'N',     'GAC': 'D',
    'UAA': 'stop',  'CAA': 'Q',     'AAA': 'K',     'GAA': 'E',
    'UAG': 'stop',  'CAG': 'Q',     'AAG': 'K',     'GAG': 'E',
    'UGU': 'C',     'CGU': 'R',     'AGU': 'S',     'GGU': 'G',
    'UGC': 'C',     'CGC': 'R',     'AGC': 'S',     'GGC': 'G',
    'UGA': 'stop',  'CGA': 'R',     'AGA': 'R',     'GGA': 'G',
    'UGG': 'W',     'CGG': 'R',     'AGG': 'R',     'GGG': 'G'
}

def main(rna_string):
    threeps = chunks(rna_string, 3)

    protein_string = []
    for codon in threeps:
        if codon_to_protein(codon) == 'stop':
            break

        protein_string += codon_to_protein(codon)

    print "".join(protein_string)

    return "".join(protein_string)




def codon_to_protein(codon):
    return RNA_CODON_TABLE[codon]

if __name__ == "__main__":
    ## Test
    # main(SAMPLE_DATASET)
    assert main(SAMPLE_DATASET) == SAMPLE_OUTPUT

    ## Prod
    with open("./datasets/rosalind_proc.txt", 'r') as fptr:
       protein_string = main(fptr.read().strip())