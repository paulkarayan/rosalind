# Given: A list L containing 2n+3 positive real numbers (n<=100). The first number 
# in L is the parent mass of a peptide P, and all other numbers represent the masses 
# of some b-ions and y-ions of P (in no particular order). You may assume that if 
# the mass of a b-ion is present, then so is that of its complementary y-ion, and vice-versa.

# Return: A protein string t of length n for which there exist two positive real 
# numbers w1 and w2 such that for every prefix p and suffix s of t, each of w(p)+w1
#  and w(s)+w2 is equal to an element of L. (In other words, there exists a protein string whose t-prefix 
# and t-suffix weights correspond to the non-parent mass values of L.) If multiple 
# solutions exist, you may output any one.

from utils import MASS_TABLE

## test cases
SAMPLE_DATASET = """1988.21104821
610.391039105
738.485999105
766.492149105
863.544909105
867.528589105
992.587499105
995.623549105
1120.6824591
1124.6661391
1221.7188991
1249.7250491
1377.8200091"""
SAMPLE_OUTPUT = "KEKEP"


def main(input_data):
    data = input_data.split("\n")
    parent_mass = float(data[0])
    ion_masses = map(float, data[1:])

    # let's find the closest pair of ions - minimize their distance from 
    # parent mass. This means we'll have the b and y ion pairs to work with later.
    pairs = list()
    for idx in range(len(ion_masses)):
        difference = 1000
        closest_partner = 0
        for mass in ion_masses:
            if abs(parent_mass - mass - ion_masses[idx]) < difference:
                difference = abs(parent_mass - mass - ion_masses[idx])
                closest_partner = mass
        pairs.append((ion_masses[idx], closest_partner))

    print pairs

    # ensure prefix < suffix
    clean_pairs = [pair for pair in pairs if pair[0] < pair[1]]
    print clean_pairs

    # remove pairs by smallest distance first
    sequence = ''




if __name__ == "__main__":
    ## Test
    # main(SAMPLE_DATASET)
    assert main(SAMPLE_DATASET) == SAMPLE_OUTPUT

    ## Prod
    #with open("./datasets/rosalind_XXX.txt", 'r') as fptr:
        # dna = fptr.read().strip()