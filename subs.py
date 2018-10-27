# Given: Two DNA strings s and t (each of length at most 1 kbp).
# Return: All locations of t as a substring of s.

# Remember, this is 1-based indexing!




## test cases
SAMPLE_DATASET = """GATATATGCATATACTT
                    ATAT"""
SAMPLE_OUTPUT = "2 4 10"


def main(input):
    answer = ""
    s, t = input.split("\n")[0].strip(), input.split("\n")[1].strip()
    # print s,t
    for idx, _ in enumerate(s):
        
        window = s[idx-1:idx - 1 + len(t)]
        if window < len(t):
            break
        if window == t:
            # print idx
            answer += "{} ".format(idx)
    return answer.strip()


if __name__ == "__main__":
    ## Test
    print main(SAMPLE_DATASET)
    assert main(SAMPLE_DATASET) == SAMPLE_OUTPUT

    # Prod
    with open("./datasets/rosalind_subs.txt", 'r') as fptr:
        input_strings = fptr.read().strip()
        print main(input_strings)
