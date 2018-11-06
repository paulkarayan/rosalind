# Given: Two DNA strings s and t (each of length at most 1 kbp) in FASTA format.
# Return: One collection of indices of s in which the symbols of t appear as a 
# subsequence of s. If multiple solutions exist, you may return any one.

from utils import fasta_breakup

## test cases
SAMPLE_DATASET = """>Rosalind_14
ACGTACGTGACG
>Rosalind_18
GTA"""
SAMPLE_OUTPUT = "3 8 10"


def main(fasta_block):
    dna_dict = fasta_breakup(fasta_block)
    print dna_dict

    #get index of first symbol
    # search_string, target_dna = dna_dict.values()
    target_dna, search_string = dna_dict.values()

    print target_dna, search_string    
    # target_dna, search_string = list(target_dna), list(search_string)
    start_pos = 0
    results = list()
    for search_symbol in search_string:
        for idx in range(start_pos, len(target_dna)):
            # print idx, target_dna[idx], search_symbol
            if search_symbol == target_dna[idx]:
                # print search_symbol, idx + 1, "<--breaker"
                start_pos = idx + 1
                results.append(idx + 1)
                break
    results = map(str, results)
    print results, type(results)
    print " ".join(results)
    return results


if __name__ == "__main__":
    ## Test
    # main(SAMPLE_DATASET)
    # assert main(SAMPLE_DATASET) == SAMPLE_OUTPUT

    ## Prod
    # with open("./datasets/rosalind_sseq_1.txt", 'r') as fptr:
    #     dna_block = fptr.read().strip()
    #     main(dna_block)
    with open("./datasets/rosalind_sseq.txt", 'r') as fptr:
        dna_block = fptr.read().strip()
        main(dna_block)