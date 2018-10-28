## NOTE: I think this works, but I can't pass the test. I wonder if values changed?

# Given: The UniProt ID of a protein.
# Return: A list of biological processes in which the protein is involved (biological processes 
# are found in a subsection of the protein's "Gene Ontology" (GO) section).

from Bio import ExPASy
from Bio import SwissProt


## test cases
SAMPLE_DATASET = "Q5SLP9"
SAMPLE_OUTPUT = """DNA recombination
DNA repair
DNA replication"""


def main(protein_id):
    handle = ExPASy.get_sprot_raw(protein_id) #you can give several IDs separated by commas
    record = SwissProt.read(handle) # use SwissProt.parse for multiple proteins

    answer = ""
    for r in record.cross_references:
        print r
        if r[0] == "GO":
            if r[2].split(":")[0] == 'P':
                answer += r[2].split(":")[1] + "\n"

    return answer.strip()


if __name__ == "__main__":
    ## Test
    # main(SAMPLE_DATASET)
    assert main(SAMPLE_DATASET) == SAMPLE_OUTPUT

    ## Prod
    prod = "Q6Z5M0"
    print main(prod)

