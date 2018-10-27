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

def main(dataset):
    arrays = dataset.split("\n")
    del arrays[0]
    answer = ""

    for array in arrays:
        array = map(int, array.split(" "))

        # print array
        stopper = 0
        for idx, item in enumerate(array):
            # print idx, item
            if stopper == 1:
                answer += "{} {}\n".format(*values)
                break
            for idxtwo, itemtwo in enumerate(array):
                # print idx, item, idxtwo, itemtwo, answer, stopper
                if item == -itemtwo:
                    stopper = 1
                    values = (idx + 1, idxtwo + 1)
                    # print values, "<--- values"
                    break
        if stopper != 1:
            answer += " -1 \n"
    print answer 
    return answer.strip()


if __name__ == "__main__":
    ## Test
    # main(SAMPLE_DATASET)
    # assert main(SAMPLE_DATASET) == SAMPLE_OUTPUT

    # Prod
    with open("./datasets/rosalind_2sum.txt", 'r') as fptr:
       dataset = fptr.read().strip()
       main(dataset)