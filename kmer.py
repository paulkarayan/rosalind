# Order all kmers lexicographically
# The 4-mer composition of s.

import itertools

from utils import fasta_breakup

## test cases
SAMPLE_DATASET = """>Rosalind_6431
CTTCGAAAGTTTGGGCCGAGTCTTACAGTCGGTCTTGAAGCAAAGTAACGAACTCCACGG
CCCTGACTACCGAACCAGTTGTGAGTACTCAACTGGGTGAGAGTGCAGTCCCTATTGAGT
TTCCGAGACTCACCGGGATTTTCGATCCAGCCTCAGTCCAGTCTTGTGGCCAACTCACCA
AATGACGTTGGAATATCCCTGTCTAGCTCACGCAGTACTTAGTAAGAGGTCGCTGCAGCG
GGGCAAGGAGATCGGAAAATGTGCTCTATATGCGACTAAAGCTCCTAACTTACACGTAGA
CTTGCCCGTGTTAAAAACTCGGCTCACATGCTGTCTGCGGCTGGCTGTATACAGTATCTA
CCTAATACCCTTCAGTTCGCCGCACAAAAGCTGGGAGTTACCGCGGAAATCACAG"""
SAMPLE_OUTPUT = """4 1 4 3 0 1 1 5 1 3 1 2 2 1 2 0 1 1 3 1 2 1 3 1 1 1 1 2 2 5 1 3 0 2 2 1 1 1 1 3 1 0 0 1 5 5 1 5 0 2 0 2 1 2 1 1 1 2 0 1 0 0 1 1 3 2 1 0 3 2 3 0 0 2 0 8 0 0 1 0 2 1 3 0 0 0 1 4 3 2 1 1 3 1 2 1 3 1 2 1 2 1 1 1 2 3 2 1 1 0 1 1 3 2 1 2 6 2 1 1 1 2 3 3 3 2 3 0 3 2 1 1 0 0 1 4 3 0 1 5 0 2 0 1 2 1 3 0 1 2 2 1 1 0 3 0 0 4 5 0 3 0 2 1 1 3 0 3 2 2 1 1 0 2 1 0 2 2 1 2 0 2 2 5 2 2 1 1 2 1 2 2 2 2 1 1 3 4 0 2 1 1 0 1 2 2 1 1 1 5 2 0 3 2 1 1 2 2 3 0 3 0 1 3 1 2 3 0 2 1 2 2 1 2 3 0 1 2 3 1 1 3 1 0 1 1 3 0 2 1 2 2 0 2 1 1"""


def main(fasta_block):
    dna_dict = fasta_breakup(fasta_block)
    dna = dna_dict.values()[0]

    #generate kmer perms
    repeats = 4
    alphabet = "A C G T"
    perms = ["".join(x) for x in itertools.product(alphabet.replace(" ", ""), repeat=int(repeats))]
    results = [[0] * len(perms)]
    
    for idx in range(len(dna)):
        
        try:
            results[0][perms.index(dna[idx:idx+4])] += 1
        except Exception as e:
            print dna[idx:idx+4], "<-- eror", e
    
    return " ".join(map(str, results[0]))

if __name__ == "__main__":
    ## Test
    print main(SAMPLE_DATASET)

    # import difflib
    # d = difflib.Differ()
    # diff = d.compare(main(SAMPLE_DATASET), SAMPLE_OUTPUT)
    # print '\n'.join(diff)

    assert main(SAMPLE_DATASET) == SAMPLE_OUTPUT

    ## Prod
    with open("./datasets/rosalind_kmer.txt", 'r') as fptr:
        fasta_block = fptr.read().strip()
    with open("./datasets/output_kmer.txt", 'w') as fptr:
        fptr.write(main(fasta_block))