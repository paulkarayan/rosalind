# Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.
# Return: The adjacency list corresponding to O3. You may return edges in any order.

from utils import fasta_breakup

## test cases
SAMPLE_DATASET = """>Rosalind_0498
                    AAATAAA
                    >Rosalind_2391
                    AAATTTT
                    >Rosalind_2323
                    TTTTCCC
                    >Rosalind_0442
                    AAATCCC
                    >Rosalind_5013
                    GGGTGGG"""

SAMPLE_OUTPUT = """Rosalind_0498 Rosalind_2391
Rosalind_0498 Rosalind_0442
Rosalind_2391 Rosalind_2323"""


def main(dataset):
    fasta_block = fasta_breakup(dataset)
    edges = []
    for key, value in fasta_block.items():
        left = value[-3:]        
        for key_two, value_two in fasta_block.items():
            # print key, key_two, left, right
            if key == key_two:
                continue
            right = value_two[:3]
            if left == right:
                edges.append((key, key_two))
    
    for edge in edges:
        print "{0} {1}".format(*edge)



if __name__ == "__main__":
    ## Test
    # main(SAMPLE_DATASET)
    # assert main(SAMPLE_DATASET) == SAMPLE_OUTPUT ## would need to use unit test

    # Prod
    with open("./datasets/rosalind_grph.txt", 'r') as fptr:
        fasta = fptr.read().strip()
        main(fasta)
