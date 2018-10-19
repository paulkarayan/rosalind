# general idea - select a "pivot" value to assist in splitting list
# move items on wrong side of pivot and converge on split point
# to find location of pivot in sorted list

# first, set pivot value (best random, but can also be first item on list)
# increment leftmark until we locate value > pivot value
# decrement rightmark until we find value < pivot value
# exchange items under left and right marks
# split lists at the pivot point and recurse
# --> note that we guaranteed that the halves are larger/smaller than pivot
#     so we don't have to spend time merging them later!

import random

#return true if value at param 1 < value at param 2
def compare(indexable, alpha, beta):
    return indexable[alpha] < indexable[beta]

#swap locations of param1 and param 2 values
def swap(indexable, alpha, beta):
    indexable[alpha], indexable[beta] = indexable[beta], indexable[alpha]


from random import randrange
def rand_list(length, limit):
    return [randrange(1, limit) for alpha in range(length)]

lister = rand_list(10, 10)


def quick_sort(indexable, start=None, end=None):

    #handle initial case
    if start is None:
        start = 0
    if end is None:
        end = len(indexable) - 1

    #if we haven't reached base case
    if start < end:

        splitpoint = partition(indexable, start, end)

        quick_sort(indexable, start, splitpoint - 1)
        quick_sort(indexable, splitpoint + 1, end)


def partition(indexable, start, end):
    pivot = random.randrange(end - start) + start
    #move pivot to the leftmost position
    swap(indexable, pivot, start)
    pivotvalue = indexable[start]

    leftmark = start+1
    rightmark = end

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

    #now we're done, so swap the pivot into the split point
    swap(indexable, start, rightmark)
    #return the split point
    return rightmark

lister = [54,26,93,17,77,31,44,55,20]
quick_sort(lister)
# print lister
