# An array A[1..n] is said to have a majority element if more than half of its entries are the same.

# Given: A positive integer k<=20, a positive integer n<=104, and k arrays of size n containing positive integers not exceeding 105.
# Return: For each array, output an element of this array occurring strictly more than n/2 times if such element exists, and "-1" otherwise.

from __future__ import division
import collections

## test cases
SAMPLE_DATASET = """4 8
5 5 5 5 5 5 5 5
8 7 7 7 1 7 3 7
7 1 6 5 10 100 1000 1
5 1 6 7 1 1 10 1"""
SAMPLE_OUTPUT = "5 7 -1 -1"


def main(dataset):
    arrays = dataset.split("\n")
    del arrays[0]
    answer = ""
    for array in arrays:
        sp_array = array.split(" ")
        freq = collections.Counter(sp_array)
        most_common = freq.most_common(1)[0]
        if most_common[1] > (len(sp_array) / 2):
            answer += " " + str(most_common[0])
        else:
            answer += " -1"
    return answer.strip()


if __name__ == "__main__":
    ## Test
    print main(SAMPLE_DATASET)
    assert main(SAMPLE_DATASET) == SAMPLE_OUTPUT

    ## Prod
    with open("./datasets/rosalind_maj.txt", 'r') as fptr:
       dataset = fptr.read().strip()
       print main(dataset)

# notes:
# If it is possible for the elements to caste their vote for themselves then the majority element 
# if exist will win as it occurs more than n>2 times. So we will keep track of current majority 
# element and its count. If the count is zero, the current element will be majority element and 
# we increment the count. If the next number is same as majority element, we increment count by 
# one(elements are casting vote for themselves) else decrement it by one(when we cast vote for our self, 
# the vote count for others will obliviously decrease). We will continue this process for all the elements 
# and at the end majority element variable contains required answer if exists.