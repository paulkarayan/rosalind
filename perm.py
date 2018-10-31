# Given: A positive integer n<=7.
# Return: The total number of permutations of length n, followed by a list of all such permutations (in any order).
from itertools import permutations

## test cases
SAMPLE_DATASET = "3"
SAMPLE_OUTPUT = """6
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1"""


def main(n_integer):
    perms = [list(perm) for perm in permutations(range(1, int(n_integer)+1))]

    print str(len(perms))
    for perm in perms:
        print " ".join(map(str,perm))


if __name__ == "__main__":
    ## Test
    # main(SAMPLE_DATASET)
    # I'm being lazy, we should iterate the list of perms and check if they're in it

    ## Prod
    main("6")