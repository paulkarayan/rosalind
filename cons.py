
# Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.
# Return: A consensus string and profile matrix for the collection. 
# (If several possible consensus strings exist, then you may return any one of them.)

# import numpy as np
# from numpy import array as arr


from utils import fasta_breakup

## test cases
SAMPLE_DATASET = """>Rosalind_1
ATCCAGCT
>Rosalind_2
GGGCAACT
>Rosalind_3
ATGGATCT
>Rosalind_4
AAGCAACC
>Rosalind_5
TTGGAACT
>Rosalind_6
ATGCCATT
>Rosalind_7
ATGGCACT"""
SAMPLE_OUTPUT = """ATGCAACT
A: 5 1 0 0 5 5 0 0
C: 0 0 1 4 2 0 6 1
G: 1 1 6 3 0 1 0 0
T: 1 5 0 0 0 1 1 6"""



def main(dataset):
    fasta_block = fasta_breakup(dataset)
    result_matrix = lol_version(fasta_block)
    cons = consensus(result_matrix)
    return "{}\nA: {}\nC: {}\nG: {}\nT: {}".format(cons, 
                                              " ".join(map(str, result_matrix['A'])), 
                                              " ".join(map(str, result_matrix['C'])),
                                              " ".join(map(str, result_matrix['G'])),
                                              " ".join(map(str, result_matrix['T'])))

def lol_version(fasta_block):
    len_dna = len(fasta_block.values()[0])

    result_matrix =  {"A": [0] * len_dna , "C": [0] * len_dna, 
                      "G": [0] * len_dna, "T": [0] * len_dna}    

    for label, dna_string in fasta_block.items():
        for idx, base in enumerate(dna_string):
            result_matrix[base][idx] +=1
    return result_matrix

def consensus(result_matrix):
    consensus = [('A', 0) for item in range(len(result_matrix['A']))]
    for k, x in result_matrix.items():
        for idx in range(len(x)):
            if x[idx] > consensus[idx][1]:
                consensus[idx] = (k, x[idx])
    return "".join([item[0] for item in consensus])

if __name__ == "__main__":
    ## Test
    assert main(SAMPLE_DATASET) == SAMPLE_OUTPUT

    ## Prod
    with open("./datasets/rosalind_cons.txt", 'r') as fptr:
        fastas = fptr.read().strip()
        my_output = main(fastas)
    with open("./datasets/output_cons.txt", 'w') as fptr:
        fptr.write(my_output)


    # with open("./datasets/output_cons_1.txt", 'r') as fptr:
    #     output = fptr.read().strip()

    # with open("./datasets/rosalind_cons_1.txt", 'r') as fptr:
    #     fastas = fptr.read().strip()
    #     my_output = main(fastas)

    #     import difflib

    #     d = difflib.Differ()
    #     diff = d.compare(output.splitlines(), my_output.splitlines())
    #     print '\n'.join(diff)