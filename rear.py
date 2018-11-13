# inversions
# produce reversal distance from each permutation pair

## test cases
SAMPLE_DATASET = """1 2 3 4 5 6 7 8 9 10
3 1 5 2 7 4 9 6 10 8

3 10 8 2 5 4 7 1 6 9
5 2 3 1 7 4 10 8 6 9

8 6 7 9 4 1 3 10 2 5
8 2 7 6 9 1 5 3 10 4

3 9 10 4 1 8 6 7 5 2
2 9 8 5 1 7 3 4 6 10

1 2 3 4 5 6 7 8 9 10
1 2 3 4 5 6 7 8 9 10"""

SAMPLE_OUTPUT = "9 4 5 7 0"


def main(input_block):
    input_block = input_block.split("\n")
    no_space = [num for num in input_block if num != '']
    results = list()
    print no_space
    for idx, item in enumerate(no_space):
        if not idx % 2:
            pair_one, pair_two = no_space[idx], no_space[idx+1]

            if pair_one == pair_two:
                results.append(0)
    return results
    
if __name__ == "__main__":
    ## Test
    print main(SAMPLE_DATASET)
    # assert main(SAMPLE_DATASET) == SAMPLE_OUTPUT

    ## Prod
    #with open("./datasets/rosalind_XXX.txt", 'r') as fptr:
        # dna = fptr.read().strip()