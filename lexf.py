import itertools

SAMPLE_DATASET = """A C G T
2"""

SAMPLE_OUTPUT = """AA
AC
AG
AT
CA
CC
CG
CT
GA
GC
GG
GT
TA
TC
TG
TT"""

## NOTE: https://docs.python.org/2/library/itertools.html#itertools.product
# This pattern creates a lexicographic ordering
# For example, product(A, repeat=4) means the same as product(A, A, A, A).

def main(input_text):
    alphabet, repeats = input_text.split("\n")
    results = [x for x in itertools.product(alphabet.replace(" ", ""), repeat=int(repeats))]

    return_string = ''
    for pair in results:
        return_string += "".join(pair) + "\n"
    return return_string.strip()

if __name__ == "__main__":
    ## Test
    # print main(SAMPLE_DATASET)
    assert main(SAMPLE_DATASET) == SAMPLE_OUTPUT

    ## Prod
    with open("./datasets/rosalind_lexf.txt", 'r') as fptr:
        input_text = fptr.read().strip()
        print main(input_text)