## Heap notes:
# http://interactivepython.org/courselib/static/pythonds/Trees/BinaryHeapImplementation.html
# https://codereview.stackexchange.com/questions/156027/implementing-heap-in-python
import operator

import heapq

## test cases
SAMPLE_DATASET = """5
1 3 5 7 2"""
SAMPLE_OUTPUT = "7 5 1 3 2"


def main(dataset):
    array = dataset.split("\n")[1].strip()
    
    heap = heapsort_max(array.split(" ")[::-1])
    # print " ".join(heap)

    heap = BinHeap()
    for item in array.split(" ")[::-1]:
        heap.insert(item)
    # print heap
    # return the second one, i guess
    return heap

def heapsort_max(iterable):
    return heapq.nlargest(len(iterable), iterable)

def heapsort(iterable):
    h = []
    for value in iterable:
        heappush(h, value)
    return [heappop(h) for i in range(len(h))]

class BinHeap(object):
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    def _perc_up(self, i):
        while i // 2 > 0:
            if self.heap_list[i] > self.heap_list[i // 2]:
                tmp = self.heap_list[i // 2]
                self.heap_list[i // 2] = self.heap_list[i]
                self.heap_list[i] = tmp
            i = i // 2

    def insert(self, k):
        self.heap_list.append(k)
        self.current_size = self.current_size + 1
        self._perc_up(self.current_size)

    def __repr__(self):
        tmp = self.heap_list
        del tmp[0]
        return " ".join(tmp)


if __name__ == "__main__":
    ## Test
    main(SAMPLE_DATASET)
    # assert main(SAMPLE_DATASET) == SAMPLE_OUTPUT

    ## Prod
    with open("./datasets/rosalind_hea.txt", 'r') as fptr:
       dataset = fptr.read().strip()
       output_data = main(dataset)
    with open("./datasets/output_hea.txt", 'w') as fptr:
        fptr.write(list(output_data))