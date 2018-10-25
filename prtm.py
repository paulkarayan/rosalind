# Given: A protein string P of length at most 1000 aa.
# Return: The total weight of P. Consult the monoisotopic mass table.


MASS_TABLE = {'A': 71.03711,
            'C': 103.00919,
            'D': 115.02694,
            'E': 129.04259,
            'F': 147.06841,
            'G': 57.02146,
            'H': 137.05891,
            'I': 113.08406,
            'K': 128.09496,
            'L': 113.08406,
            'M': 131.04049,
            'N': 114.04293,
            'P': 97.05276,
            'Q': 128.05858,
            'R': 156.10111,
            'S': 87.03203,
            'T': 101.04768,
            'V': 99.06841,
            'W': 186.07931,
            'Y': 163.06333
            }
	

## test cases
SAMPLE_DATASET = "SKADYEK"
SAMPLE_OUTPUT = "821.392"


def main(protein_string):
    print round(sum([MASS_TABLE[amino_acid] for amino_acid in protein_string]),3)
    return str(round(sum([MASS_TABLE[amino_acid] for amino_acid in protein_string]),3))


if __name__ == "__main__":
    ## Test
    # main(SAMPLE_DATASET)
    assert main(SAMPLE_DATASET) == SAMPLE_OUTPUT

    ## Prod
    with open("./datasets/rosalind_prtm.txt", 'r') as fptr:
       protein_string = fptr.read().strip()
    main(protein_string)