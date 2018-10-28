# Given: Six nonnegative integers, each of which does not exceed 20,000. 
# The integers correspond to the number of couples in a population possessing each genotype pairing 
# for a given factor. In order, the six given integers represent the number of couples having the following genotypes:
# AA-AA
# AA-Aa
# AA-aa
# Aa-Aa
# Aa-aa
# aa-aa
# Return: The expected number of offspring displaying the dominant phenotype 
# in the next generation, under the assumption that every couple has exactly two offspring.


from __future__ import division

## test cases
SAMPLE_DATASET = "1 0 0 1 0 1"
SAMPLE_OUTPUT = "3.5"


def main(dataset):
    splitter = map(int, dataset.split(" "))

    result = 1 *  splitter[0] * 2  +\
             1 *  splitter[1] * 2  +\
             1 * splitter[2] * 2  +\
             0.75 * splitter[3] * 2  +\
             0.5 * splitter[4] * 2  +\
             0 * splitter[5] * 2 

    return result


if __name__ == "__main__":
    ## Test
    print main(SAMPLE_DATASET)
    # assert main(SAMPLE_DATASET) == SAMPLE_OUTPUT   ## need to round...

    ## Prod
    print main("16689 18668 16748 17611 16606 16801")
