# Given: A collection of k (k<=100) DNA strings of length at most 1 kbp each in FASTA format.
# Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)

from utils import fasta_breakup

## test cases
SAMPLE_DATASET = """>Rosalind_1
GATTACA
>Rosalind_2
TAGACCA
>Rosalind_3
ATACA"""
SAMPLE_OUTPUT = "AC"


def main(fasta_block):
    dna_dict = fasta_breakup(fasta_block)

    # find smallest dna - since none can be longer than this
    smallest_dna = min(dna_dict.values(), key=len)
    
    # remove the one we're comparing too. 
    dnas = dna_dict.values()
    dnas.remove(smallest_dna)
    # can reverse this to do faster...
    for sub_length in range(len(smallest_dna), 0, -1):
        # go until you are smaller than sub_length
        for pos in range(0, len(smallest_dna)-sub_length+1):
            substring = smallest_dna[pos:pos+sub_length]

            if all(substring in dna for dna in dnas):
                print "hooray substring: {}".format(substring)
                return substring
    return False

if __name__ == "__main__":
    ## Test
    main(SAMPLE_DATASET)
## AC or AT -> can be any of the substrings of same length!
    # assert main(SAMPLE_DATASET) == SAMPLE_OUTPUT

    ## Prod
    with open("./datasets/rosalind_lcsm.txt", 'r') as fptr:
        dna = fptr.read().strip()
        print main(dna)