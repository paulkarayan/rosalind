# shortest common superstring

# http://www.cs.jhu.edu/~langmea/resources/lecture_notes/assembly_scs.pdf
import itertools

from utils import fasta_breakup
## test cases
SAMPLE_DATASET = """>Rosalind_56
                    ATTAGACCTG
                    >Rosalind_57
                    CCTGCCGGAA
                    >Rosalind_58
                    AGACCTGCCG
                    >Rosalind_59
                    GCCGGAATAC"""
SAMPLE_OUTPUT = "ATTAGACCTGCCGGAATAC"


def main(fasta_block):
    dna_dict = fasta_breakup(fasta_block)
    print dna_dict
    SEQUENCES = dna_dict.values()
    #generate the naive superstring
    longest_naive = ''.join(SEQUENCES)
    # assert that this is indeed a superstring
    assert all(seq in longest_naive for seq in SEQUENCES)

    # see: https://stackoverflow.com/questions/20071702/more-efficient-algorithm-for-shortest-superstring-search
    current_shortest = longest_naive
    trim = len(current_shortest)-1
    seen_prefixes = set()

    # try every permutation of sequences so we ensure we get smallest superstring
    for perm in itertools.permutations(SEQUENCES):
        # concat the strings, then trim off one less than the current shortest
        # this becomes the prefix that we'll search by
        candidate_string = ''.join(perm)[:trim]
        print perm, trim, candidate_string
        # if we've already tried this prefix, skip to the next one to try
        if candidate_string in seen_prefixes:
            continue
        seen_prefixes.add(candidate_string)

    #     while all(seq in longest_naive for seq in SEQUENCES):
    #         current_shortest = candidate_string
    #         candidate_string = candidate_string[:-1]
    #         trim = len(current_shortest)-1
    # return current_shortest


    print longest_naive

    return 


if __name__ == "__main__":
    ## Test
    # main(SAMPLE_DATASET)
    assert main(SAMPLE_DATASET) == SAMPLE_OUTPUT

    ## Prod
    #with open("./datasets/rosalind_XXX.txt", 'r') as fptr:
        # dna = fptr.read().strip()
