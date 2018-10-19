#stumped by how to do this aside from an actual iterative sort
from qs import quick_sort

SAMPLE_INPUT = """9
4 5 6 4 1 2 5 7 4
"""

real_input = open('datasets/rosalind_par3.txt').read().strip()

def main(input=SAMPLE_INPUT):
    listers = input.splitlines()
    lister = list(map(int, listers[1].split()))
    quick_sort(lister)

    print " ".join(map(str, lister))


if __name__ == '__main__':
    main(input=real_input)
    # main()
