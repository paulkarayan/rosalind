from utils import MASS_TABLE

## test cases
SAMPLE_DATASET = """3524.8542
3710.9335
3841.974
3970.0326
4057.0646"""
SAMPLE_OUTPUT = "WMQS"


def main(weights):
    weights = map(float, weights.split("\n"))
    vals = map(float, MASS_TABLE.values())
    vals = [round(x, 2) for x in vals]
    inv_mass_lookup = dict(zip(vals, MASS_TABLE.keys()))
    print weights
    # for each addtl weight, get the residue that differs
    residues = ''
    for idx, weight in enumerate(range(len(weights)-1)):
        residues += inv_mass_lookup[round(weights[idx+1] - weights[idx], 2)]

    return residues

if __name__ == "__main__":
    ## Test
    assert main(SAMPLE_DATASET) == SAMPLE_OUTPUT

    ## Prod
    with open("./datasets/rosalind_spec.txt", 'r') as fptr:
        weights = fptr.read().strip()
        print main(weights)
