SAMPLE_INPUT = """4
2 4 10 18
3
-5 11 12
"""

real_input = open('datasets/rosalind_mer.txt').read().strip()

def main(input=SAMPLE_INPUT):
    listers = input.splitlines()
    left_list = list(map(int, listers[1].split()))
    right_list = list(map(int, listers[3].split()))

    print " ".join(map(str, merge_two_sorted_arrays(left_list, right_list)))


def merge_two_sorted_arrays(left, right):
    #since you've been handed two separate lists ordered from
    #smallest to largest, compare the least value of A to least
    #value of B. remove the lesser value and append to C.
    #when one list is exhausted, append remaining vals onto C
    #in order.

    result = []
    left_idx = right_idx = 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    #drain the remaining lists...
    for pos in range(left_idx, len(left)):
        result.append(left[pos])

    for pos in range(right_idx, len(right)):
        result.append(right[pos])

    return result

if __name__ == '__main__':
    main(input=real_input)
