#longest increasing subsequence, followed by longest decreasing subsequence
# https://en.wikipedia.org/wiki/Longest_increasing_subsequence
# https://www.geeksforgeeks.org/longest-increasing-subsequence-dp-3/

## test cases
SAMPLE_DATASET = """5
5 1 4 2 3"""
SAMPLE_OUTPUT = """1 2 3
5 4 2"""


def main(input_data):
    perm_length, perm = input_data.split("\n")
    perm_length = int(perm_length)
    perm = map(int, perm.split(" "))


    for idx in range(perm_length):
        print perm[idx:]
        print lgis(perm[idx:])

def lgis(array):
    longest_seq, sequence = [array[0]], [array[0]]
    for idx in range(len(array)-1):
        for inner_idx in range(idx+1, len(array)):
            print idx, array[idx], array[inner_idx], inner_idx
            if array[idx] < array[inner_idx]:
                print "bigger", array[idx], array[inner_idx]
                sequence.append(array[inner_idx])
                print sequence, longest_seq, "*** seq check"
                if len(sequence) >= len(longest_seq):
                    longest_seq = sequence
                    sequence = [array[0]]
        print longest_seq, array[idx], "<---longest"

if __name__ == "__main__":
    ## Test
    print main(SAMPLE_DATASET)
    assert main(SAMPLE_DATASET) == SAMPLE_OUTPUT

    ## Prod
    #with open("./datasets/rosalind_XXX.txt", 'r') as fptr:
        # dna = fptr.read().strip()