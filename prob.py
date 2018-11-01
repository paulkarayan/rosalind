# Given: A DNA string s of length at most 100 bp and an array A containing at most 20 numbers between 0 and 1.

# Return: An array B having the same length as A in which B[k] represents the common logarithm of the 
# probability that a random string constructed with the GC-content found in A[k] will match s exactly.

from __future__ import division

import math

## test cases
SAMPLE_DATASET = """ACGATACAA
0.129 0.287 0.423 0.476 0.641 0.742 0.783"""
SAMPLE_OUTPUT = "-5.737 -5.217 -5.263 -5.360 -5.958 -6.628 -7.009"


def main(input_data):
    dna_string, array_string = input_data.split("\n")
    array = array_string.split(" ")

    result = list()
    for item in array:
        gc_prob = float(item) / 2
        at_prob = (1 - float(item)) / 2

        PROB_MAP = {
            "A": at_prob,
            "T": at_prob,
            "G": gc_prob,
            "C": gc_prob
        }
        match_prob = 0
        for base in dna_string:
            #apparently more accurate to log here than later.
            match_prob += math.log10(PROB_MAP[base])
        result.append("%.3f" % match_prob)

    print " ".join(result)
    return " ".join(result)

if __name__ == "__main__":
    ## Test
    # main(SAMPLE_DATASET)
    assert main(SAMPLE_DATASET) == SAMPLE_OUTPUT

    # Prod
    with open("./datasets/rosalind_prob.txt", 'r') as fptr:
        input_data = fptr.read().strip()
        main(input_data)