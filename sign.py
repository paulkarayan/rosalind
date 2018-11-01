from itertools import permutations

## test cases
SAMPLE_DATASET = "2"
SAMPLE_OUTPUT = """8
-1 -2
-1 2
1 -2
1 2
-2 -1
-2 1
2 -1
2 1"""


def main(n_integer):
    n_integer = int(n_integer)
    pos_seeds = [x for x in range(1, n_integer + 1)]
    neg_seeds = [x for x in range(-n_integer, 0)]
    seed_values = pos_seeds + neg_seeds
    perms = permutations(seed_values, n_integer)
   
    # can't have -1 and 1 ... this filters down so each signed digit only shows up once
    filtered_perms = [x for x in perms if set(range(1, n_integer+1)) == set(map(abs,x))]
    
    print str(len(filtered_perms))
    for p in filtered_perms:
        print " ".join(map(str, p))
 
if __name__ == "__main__":
    ## Test
    main(SAMPLE_DATASET)

    ## Prod
    main(3)
