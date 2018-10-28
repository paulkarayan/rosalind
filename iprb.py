# Given: Three positive integers k, m, and n, representing a population containing 
# k+m+n organisms: k individuals are homozygous dominant for a factor, m are heterozygous, 
# and n are homozygous recessive.

# Return: The probability that two randomly selected mating organisms will produce 
# an individual possessing a dominant allele (and thus displaying the dominant phenotype). 
# Assume that any two organisms can mate.
from __future__ import division

## test cases
SAMPLE_DATASET = "2 2 2"
SAMPLE_OUTPUT = "0.78333"


def main(dataset):
    splitter = map(int, dataset.split(" "))
    total = sum(splitter)
    k, m, n = splitter[0], splitter[1], splitter[2]

    result = 1 * (k / total) +\
             1 * (m / total) * (k / (total - 1)) +\
             0.75 * (m / total) * ((m - 1) / (total - 1)) +\
             0.5 * (m / total) * (n / (total - 1)) +\
             1 * (n / total) * (k / (total - 1)) +\
             0.5 * (n / total) * (m / (total - 1)) +\
             0 * (n / total)

    return result


if __name__ == "__main__":
    ## Test
    print main(SAMPLE_DATASET)
    # assert main(SAMPLE_DATASET) == SAMPLE_OUTPUT   ## need to round...

    ## Prod
    print main("26 15 30")
