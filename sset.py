# Our first question is to count the total number of possible subsets of a given set.

# Given: A positive integer n (n<=1000).
# Return: The total number of subsets of {1,2,...,n} modulo 1,000,000.

# a finite set with n elements has 2^n subsets

## test cases
SAMPLE_DATASET = 3
SAMPLE_OUTPUT = 8


def main(end):
    # print 2 ** end
    return (2 ** end) % 1000000 


if __name__ == "__main__":
    ## Test
    # main(SAMPLE_DATASET)
    assert main(SAMPLE_DATASET) == SAMPLE_OUTPUT

    ## Prod
    print main(936)