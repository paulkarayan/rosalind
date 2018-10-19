SAMPLE_INPUT = """6
6 10 4 5 1 2
"""

global compares, swaps
compares = 0
swaps = 0

real_input = open('datasets/rosalind_ins.txt').read().strip()

def main(input=SAMPLE_INPUT):
    length, lister = input.splitlines()
    input_list = list(map(int, lister.split()))

    insertion_sort(input_list)
    print swaps

def compare(indexable, alpha, beta):
    global compares
    compares += 1
    return indexable[alpha] < indexable[beta]

#swap locations of param1 and param 2 values
def swap(indexable, alpha, beta):
    global swaps
    swaps += 1
    indexable[alpha], indexable[beta] = indexable[beta], indexable[alpha]

def insertion_sort(indexable):
    #iterate the full list... but go to the end, and only go as far
    #as hasn't been gone previous
    for alpha in range(1,len(indexable)):
        beta = alpha
        while beta > 0 and compare(indexable, beta, beta - 1):
            swap(indexable, beta - 1, beta)
            beta -= 1


if __name__ == '__main__':
    main(input=real_input)
