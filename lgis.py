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
    perm = perm.split(" ")

    increasing_cache, decreasing_cache = dict(), dict()

    largest_increasing_subsequence(perm, increasing_cache, lis='')

def largest_increasing_subsequence(array, cache, lis):
    for idx in range(len(array)-1, -1, -1):
        print idx, array[idx]
        # use cache
        if array[idx] in cache:
            lis = array[idx] + cache[array[idx]]
            print lis, "<cache>"
        # if previous item is smaller (e.g. we have increasing seq)
        # append...
        if array[idx-1] < array[idx]:
            lis += str(array[idx])
            if str(array[idx]) not in cache.keys():
                cache[str(array[idx])] = lis
            elif len(lis) > cache[str(array[idx])]:
                cache[str(array[idx])].update(lis)
            else:
                print "else"
                
            print lis, "<add to cache - keep going>", cache
            continue
        else:
            lis = str(array[idx]) + lis
            cache[str(array[idx])] = lis
            print lis, "<add to cache - bust>", cache
            lis = ''


if __name__ == "__main__":
    ## Test
    # main(SAMPLE_DATASET)
    assert main(SAMPLE_DATASET) == SAMPLE_OUTPUT

    ## Prod
    #with open("./datasets/rosalind_XXX.txt", 'r') as fptr:
        # dna = fptr.read().strip()