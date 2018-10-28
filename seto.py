# Given: A positive integer n (n<=20,000) and two subsets A and B of {1,2,...,n}.
# Return: Six sets: AuB, AintersectB, A-B, B-A, A^c, and B^c
# (where set complements are taken with respect to {1,2,...,n}).


## test cases
SAMPLE_DATASET = """10
{1, 2, 3, 4, 5}
{2, 8, 5, 10}"""
SAMPLE_OUTPUT = """{1, 2, 3, 4, 5, 8, 10}
{2, 5}
{1, 3, 4}
{8, 10}
{8, 9, 10, 6, 7}
{1, 3, 4, 6, 7, 9}"""

def main(dataset):
    splitter = dataset.split("\n")
    superset = {x for x in range(1,int(splitter[0])+1)}
    # yes, i know eval is evil.
    A, B = set(eval(splitter[1])), set(eval(splitter[2]))
    union = A | B
    intersection = A & B
    AminusB = A - B
    BminusA = B - A
    Acomp = superset - A
    Bcomp = superset - B
    
    return (set_formatter(union) +"\n" + set_formatter(intersection) + "\n" +
            set_formatter(AminusB) +"\n" + set_formatter(BminusA) + "\n" +
            set_formatter(Acomp) +"\n" + set_formatter(Bcomp)
           )

def set_formatter(set_):
    """ return the expected {} str representation of a set"""
    return "{{{}}}".format(', '.join(str(e) for e in set_))


if __name__ == "__main__":
    ## Test
    print main(SAMPLE_DATASET)
    assert main(SAMPLE_DATASET) == SAMPLE_OUTPUT

    with open("./datasets/rosalind_seto_1.txt", 'r') as fptr:
        set_input = fptr.read().strip()
    with open("./datasets/output_seto_1.txt", 'r') as fptr:
        set_output = fptr.read().strip()
        assert main(set_input) == set_output

    ## Prod
    with open("./datasets/rosalind_seto.txt", 'r') as fptr:
        set_input = fptr.read().strip()
    output_data = main(set_input)
    with open("./datasets/output_seto.txt", 'w') as fptr:
        fptr.write(output_data)