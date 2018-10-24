#general idea: split the list in half, sort left and right copies,
#              merge them together

def merge_sort(indexable):

    #base case
    if len(indexable) <= 1:
        return indexable

    #split the list
    middle = len(indexable) / 2
    left = indexable[:middle]
    right = indexable[middle:]

    #sort left and right copies
    left = merge_sort(left)
    right = merge_sort(right)

    #merge left and right partitions together
    result = []
    left_idx = right_idx = 0

    #since you've been handed two separate lists ordered from
    #smallest to largest, compare the least value of A to least
    #value of B. remove the lesser value and append to C.
    #when one list is exhausted, append remaining vals onto C
    #in order.

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

from random import randrange
def rand_list(length, limit):
    return [randrange(1, limit) for alpha in range(length)]

# lister = rand_list(10, 10)
# print merge_sort(lister)

SAMPLE_DATASET = """10
20 19 35 -18 17 -20 20 1 4 4"""
SAMPLE_OUTPUT = "-20 -18 1 4 4 17 19 20 20 35"

def prepped_merge_sort(dataset):
    clean_data_list = dataset.split("\n")[1].split(" ")
    clean_data_list = map(int, clean_data_list)
    sorted_list = merge_sort(clean_data_list)
 
    return  " ".join(map(str, sorted_list))

assert prepped_merge_sort(SAMPLE_DATASET) == SAMPLE_OUTPUT

with open("./datasets/rosalind_ms.txt", 'r') as fptr:
    file_input_data = fptr.read()
    output_data = prepped_merge_sort(file_input_data)
with open("./datasets/output_ms.txt", 'w') as fptr:
    fptr.write(output_data)