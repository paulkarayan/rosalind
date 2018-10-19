# An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.
# Given a DNA string t corresponding to a coding strand, its transcribed RNA string u is
# formed by replacing all occurrences of 'T' in t with 'U' in u.

# Given: A DNA string t having length at most 1000 nt.
# Return: The transcribed RNA string of t.

## test cases
SAMPLE_DATASET = "GATGGAACTTGACTACGTAAATT"
SAMPLE_OUTPUT = "GAUGGAACUUGACUACGUAAAUU"

def main(dna_string):
    print dna_to_rna(dna_string)
    return dna_to_rna(dna_string)

def dna_to_rna(dna_string):
    return dna_string.replace('T', 'U') 

if __name__ == "__main__":
    ## Test
    # main(SAMPLE_DATASET)
    assert main(SAMPLE_DATASET) == SAMPLE_OUTPUT

    ## Prod
    with open("./datasets/rosalind_rna.txt", 'r') as fptr:
        dna = fptr.read()
        main(dna) 