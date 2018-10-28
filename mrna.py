# Given: A protein string of length at most 1000 aa.
# Return: The total number of different RNA strings from which the protein could have been 
# translated, modulo 1,000,000. (Don't neglect the importance of the stop codon in protein translation.)

from prot import RNA_CODON_TABLE

## test cases
SAMPLE_DATASET = "MA"
SAMPLE_OUTPUT = "12"


def main(protein_string):
    
    # for stop codons
    counter = 3 
    for amino_acid in protein_string:
        counter *= sum([bool(value) for key, value in RNA_CODON_TABLE.items() if value == amino_acid])
    
    print counter % 1000000
    return str(counter % 1000000) 


if __name__ == "__main__":
    ## Test
    # main(SAMPLE_DATASET)
    assert main(SAMPLE_DATASET) == SAMPLE_OUTPUT

    # Prod
    with open("./datasets/rosalind_mrna.txt", 'r') as fptr:
        protein_string = fptr.read().strip()
        main(protein_string)
