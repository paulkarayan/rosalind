# For each array A[1..n], output two different indices 
# 1<=p<q<=n such that A[p]=-A[q] if exist, 
# and "-1" otherwise.

## test cases
SAMPLE_DATASET = """4 5
2 -3 4 10 5
8 2 4 -2 -8
-5 2 3 2 -4
5 4 -5 6 8"""

SAMPLE_OUTPUT ="""-1
2 4
-1
1 3"""

# this is really a two sums problem, adding to 0
def main(dataset):
    arrays = dataset.split("\n")
    del arrays[0]
    answer = ""

    for array in arrays:
        cache = {}
        array = map(int, array.split(" "))
        # print array
        for idx, item in enumerate(array):
            if 0 - item in cache:
                answer += "{} {}\n".format(cache[-item] + 1, idx + 1)
                break
            cache[item] = idx
            if idx + 1 == len(array):
                answer += "-1\n"
        
            
    # print answer
    return answer.strip()

if __name__ == "__main__":
    ## Test
    # main(SAMPLE_DATASET)
    assert main(SAMPLE_DATASET) == SAMPLE_OUTPUT

    # Prod
    with open("./datasets/rosalind_2sum.txt", 'r') as fptr:
       dataset = fptr.read().strip()
       print main(dataset)