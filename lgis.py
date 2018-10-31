#longest increasing subsequence, followed by longest decreasing subsequence


## test cases
SAMPLE_DATASET = """5
5 1 4 2 3"""
SAMPLE_OUTPUT = """1 2 3
5 4 2"""


def main(input_data):
    perm_length, perm = input_data.split("\n")
    perm_length = int(perm_length)
    perm = perm.split(" ")
    print perm_length, perm

    # brute force 
    increasing, decreasing = list(), list()

    for pos in range(perm_length):
        current_increasing, current_decreasing = '', ''
        for idx in range(perm_length):
            print perm[pos], perm[idx], "<--index"
            if idx == 0:
                current_increasing += perm[idx]
                current_decreasing += perm[idx]
                continue
            if perm[idx] > current_increasing[-1]:
                current_increasing += perm[idx]
            if perm[idx] < current_decreasing[-1]:
                current_decreasing += perm[idx]
            print current_increasing, "<--inc", current_decreasing, "<--- dec"


if __name__ == "__main__":
    ## Test
    # main(SAMPLE_DATASET)
    assert main(SAMPLE_DATASET) == SAMPLE_OUTPUT

    ## Prod
    #with open("./datasets/rosalind_XXX.txt", 'r') as fptr:
        # dna = fptr.read().strip()