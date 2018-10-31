from scipy.special import comb


## test cases
SAMPLE_DATASET = "21 7"
SAMPLE_OUTPUT = "51200"

# number of partial perms
# Pnn = n * n -1 * n-2 etc...
# because each number you move forward, you can pick from one less option

def main(input_data):
    perms = 1
    n, k = input_data.split(" ")
    n, k = int(n), int(k)
    for idx in range(k):
        perms *= (n - idx)
        perms = perms % 1000000
    
    print perms

    return str(perms)


if __name__ == "__main__":
    ## Test
    # main(SAMPLE_DATASET)
    assert main(SAMPLE_DATASET) == SAMPLE_OUTPUT

    ## Prod
    print main("97 9")