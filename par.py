

SAMPLE_INPUT = """9
7 2 5 6 1 3 9 4 8
"""

real_input = open('datasets/rosalind_par.txt').read().strip()

def main(input=SAMPLE_INPUT):
    listers = input.splitlines()
    lister = list(map(int, listers[1].split()))
    partition(lister)

    print " ".join(map(str, lister))

#swap locations of param1 and param 2 values
def swap(indexable, alpha, beta):
    indexable[alpha], indexable[beta] = indexable[beta], indexable[alpha]

def partition(indexable):

    pivotvalue = indexable[0]

    leftmark = 1
    rightmark = len(indexable) - 1

    while 1:
        #move left and right marks if there isn't a swap needed
        while leftmark <= rightmark and indexable[leftmark] <= pivotvalue:
            leftmark += 1

        while rightmark >= leftmark and indexable[rightmark] >= pivotvalue:
            rightmark -= 1

        #if the marks crossover, we're done. break.
        if rightmark < leftmark:
            break
        # otherwise, swap values
        else:
            swap(indexable, leftmark, rightmark)

    #swap pivot value into place
    swap(indexable, 0, rightmark)

    return rightmark

if __name__ == '__main__':
    main(input=real_input)
    # main()
