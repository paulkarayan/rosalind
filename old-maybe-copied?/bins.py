#this was not immediately obvious, but we are to output the index of
#keys from the 4th line in the list on the 3rd line.
#i.e. 40 is the first key, it's index 4 (starts on 1, not 0)
from bisect import bisect_left

SAMPLE_INPUT = """5
6
10 20 30 40 50
40 10 35 15 40 20
"""

real_input = open('datasets/rosalind_bins.txt').read().strip()

def main(input=SAMPLE_INPUT):
    n, m, A, M = input.splitlines()
    M = map(int, M.split())
    A = map(int, A.split())
    result_set = []
    for element in M:
        result_set.append(binary_search(element, A))

    print " ".join(map(str, result_set))

#uses bisect_left:
#send in the element, along with a low and high limit
#The returned insertion point i partitions the array a into two halves
#here's the underlying code:
    # if lo < 0:
    #     raise ValueError('lo must be non-negative')
    # if hi is None:
    #     hi = len(a)
    # while lo < hi:
    #     mid = (lo+hi)//2
    #     if a[mid] < x: lo = mid+1
    #     else: hi = mid
    # return lo
def binary_search(element, input_list):
    pos = bisect_left(input_list, element, 0, len(input_list))
    if pos != len(input_list) and input_list[pos] == element:
        #remember, index doesn't start at 0 here
        return pos + 1
    else:
        return -1

if __name__ == '__main__':
    # main()
    main(input=real_input)
