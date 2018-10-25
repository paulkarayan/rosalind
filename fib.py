# Given: Positive integers n<=40 and k<=5.
# Return: The total number of rabbit pairs that will be present after n months, 
# if we begin with 1 pair and in each generation, every pair of reproduction-age 
# rabbits produces a litter of k rabbit pairs (instead of only 1 pair).

## this one was WILD! remember you have to clear the cache. i got into 
# weird situations, which i might fix by adding a global and using tuples.
# but i just explicitly clear the cache instead. 


## test cases
SAMPLE_DATASET = "5 3"
SAMPLE_OUTPUT = "19"

SAMPLE_DATASET_TWO = "35 4"
SAMPLE_OUTPUT_TWO = "48127306357829"


def main(dataset):
    dataset = map(int, dataset.split(" "))
    n, k = dataset[0], dataset[1]
    print fib(n, k)
    return str(fib(n, k))


# cache is generation: total pairs


def fib(n, k):
    # if you already have answer, return it
    if n in cache.keys():
        return cache[n]

    # first two generations = 1 pair
    if n == 2 or n == 1:
        cache[n] = 1
    # otherwise, caculate rabbits whilst pulling from cache
    else:
        cache[n] = fib(n-1, k) + k * fib(n-2, k)

    return cache[n]


if __name__ == "__main__":
    ## Test
    cache = {}
    # main(SAMPLE_DATASET)
    assert main(SAMPLE_DATASET) == SAMPLE_OUTPUT
    cache = {}
    assert main(SAMPLE_DATASET_TWO) == SAMPLE_OUTPUT_TWO
    cache = {}

    # Prod
    with open("./datasets/rosalind_fib.txt", 'r') as fptr:
        input_data = fptr.read().strip()
        main(input_data)