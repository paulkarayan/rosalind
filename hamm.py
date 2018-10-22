# Given two strings s and t of equal length, the Hamming distance between s and t, denoted dH(s,t), is the number of corresponding symbols that differ in s and t. See Figure 2.
# Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
# Return: The Hamming distance dH(s,t).



## test cases
SAMPLE_DATASET = """GAGCCTACTAACGGGAT
                    CATCGTAATGACGGCCT"""
SAMPLE_OUTPUT = 7

# making command decision for now that we split and strip input as part of main. 
# i dont know if that's right decision or not.

def main(dna_block):
    dna_strings = dna_block.split("\n")
    # remove empty strings, such as when you newline by accident
    dna_strings = filter(None, dna_strings)
    print dna_strings
    dna_strings = [str_.strip() for str_ in dna_strings]

    # assume dna strings is 2 long
    assert len(dna_strings) == 2
    return hamming(dna_strings[0], dna_strings[1])


def hamming(dna_string_s, dna_string_t):
    """ hamming distance is the number of positions in the strings where the corresponding
        symbols differ
    """
    assert len(dna_string_s) == len(dna_string_t), "strings must be same length"

    hamming_distance = 0
    for idx, symbol in enumerate(dna_string_s):
        if symbol != dna_string_t[idx]:
            hamming_distance += 1

    return hamming_distance

if __name__ == "__main__":
    ## Test
    print main(SAMPLE_DATASET)
    assert main(SAMPLE_DATASET), SAMPLE_OUTPUT

    ## Prod
    with open("./datasets/rosalind_hamm.txt", 'r') as fptr:
       dna_block = fptr.read()
       print main(dna_block)