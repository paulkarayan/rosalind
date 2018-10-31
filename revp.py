# Given: A DNA string of length at most 1 kbp in FASTA format.
# Return: The position and length of every reverse palindrome in the string having length between 4 and 12. 
# You may return these pairs in any order.

from utils import reverse_complement, fasta_breakup

## test cases
SAMPLE_DATASET = """>Rosalind_24
TCAATGCATGCGGGTCTATATGCAT"""
SAMPLE_OUTPUT = """4 6
5 4
6 6
7 4
17 4
18 4
20 6
21 4"""


def main(fasta_block):
    fasta_dict = fasta_breakup(fasta_block)
    dna = fasta_dict.values()[0]

    restriction_sites = []
    for block_len in range(4,14,2):
        idx = 0
        while idx <= len(dna) - block_len:
            current = dna[0+idx: block_len+idx]
            # split current in half
            if current[:(block_len/2)] == "".join(reverse_complement(current[(block_len/2):])):
                print "palindrome, yo", current, current[:(block_len/2)], "".join(reverse_complement(current[(block_len/2):]))
                restriction_sites.append([idx+1, block_len])
            idx += 1
    print restriction_sites
    return restriction_sites


if __name__ == "__main__":
    ## Test
    # main(SAMPLE_DATASET)
    processed_sample_output = [item.split(" ") for item in SAMPLE_OUTPUT.split("\n")]
    processed_sample_output = [[int(item[0]), int(item[1])] for item in processed_sample_output]

    for item in main(SAMPLE_DATASET):
        assert item in processed_sample_output

    # process to make stuff look right
    print "\n\n\n"
    for item in main(SAMPLE_DATASET):
        item = map(str, item)
        # print " ".join(item)

    ## Prod - test on working example
    with open("./datasets/output_revp_1.txt", 'r') as fptr:
        answers = fptr.read()

        processed_sample_output = [item.split(" ") for item in answers.split("\n")]
        processed_sample_output = [[int(item[0]), int(item[1])] for item in processed_sample_output]
        print processed_sample_output
        print "***************"

    with open("./datasets/rosalind_revp_1.txt", 'r') as fptr:
        dna = fptr.read().strip()
        answer = main(dna)
        for item in answer:
            # item = map(str, item)
            # print " ".join(item)
            assert item in processed_sample_output
        for item in processed_sample_output:
            assert item in answer, "this was not there {}".format(item)
    
    ## Prod - test on working example
    with open("./datasets/rosalind_revp.txt", 'r') as fptr:
        dna = fptr.read().strip()
        answer = main(dna)
        print answer
    with open('./datasets/output_revp.txt', 'w') as fptr:
        for item in answer:
            item = map(str, item)
            print item
            fptr.write(" ".join(item) + "\n")