# U always need Utils. har har.

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]

def fasta_breakup(fasta_block):
    fasta_strings = fasta_block.split(">")
    # remove empty strings, such as when you newline by accident
    fasta_strings = filter(None, fasta_strings)
    #strip whitespaces
    # fasta_strings = [str_.strip() for str_ in fasta_strings]
    fasta_strings = ["".join(str_.split(" ")) for str_ in fasta_strings]

    fasta_dict = {}

    for subunit in fasta_strings:
        fasta_label = subunit.split("\n")[0]
        bases = ''.join(subunit.split("\n")[1:])
        fasta_dict[fasta_label] = bases

    return fasta_dict