import random

#swap locations of param1 and param 2 values
def swap(indexable, alpha, beta):
    indexable[alpha], indexable[beta] = indexable[beta], indexable[alpha]


def quick_sort(indexable,first=None,last=None):

  #handle initial case
  if first is None:
    first = 0
  if last is None:
    last = len(indexable) - 1

  if first<last:

     splitpoint = partition(indexable,first,last)

     quick_sort(indexable,first,splitpoint-1)
     quick_sort(indexable,splitpoint+1,last)


def partition(indexable,first,last):

  pivot = random.randrange(last - first) + first
  #move pivot to the leftmost position
  swap(indexable, pivot, first)

  #remember that we've swapped the pivot into first position, so we
  #don't want to grab the old position!!
  pivotvalue = indexable[first]
  leftmark = first+1
  rightmark = last

  while 1:

     while leftmark <= rightmark and indexable[leftmark] <= pivotvalue:
         leftmark = leftmark + 1

     while rightmark >= leftmark and indexable[rightmark] >= pivotvalue:
         rightmark = rightmark -1

     if rightmark < leftmark:
         break
     else:
         swap(indexable, leftmark, rightmark)

  swap(indexable, first, rightmark)

  return rightmark

lister = [54,26,93,17,77,31,44,55,20]
quick_sort(lister)
print(lister)
