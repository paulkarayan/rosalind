# U always need Utils. har har.

REV_SYMBOLS = {
    "A": "T",
    "T": "A",
    "C": "G",
    "G": "C"
}

RNA_CODON_TABLE = {
    'UUU': 'F',     'CUU': 'L',     'AUU': 'I',     'GUU': 'V',
    'UUC': 'F',     'CUC': 'L',     'AUC': 'I',     'GUC': 'V',
    'UUA': 'L',     'CUA': 'L',     'AUA': 'I',     'GUA': 'V',
    'UUG': 'L',     'CUG': 'L',     'AUG': 'M',     'GUG': 'V',
    'UCU': 'S',     'CCU': 'P',     'ACU': 'T',     'GCU': 'A',
    'UCC': 'S',     'CCC': 'P',     'ACC': 'T',     'GCC': 'A',
    'UCA': 'S',     'CCA': 'P',     'ACA': 'T',     'GCA': 'A',
    'UCG': 'S',     'CCG': 'P',     'ACG': 'T',     'GCG': 'A',
    'UAU': 'Y',     'CAU': 'H',     'AAU': 'N',     'GAU': 'D',
    'UAC': 'Y',     'CAC': 'H',     'AAC': 'N',     'GAC': 'D',
    'UAA': 'stop',  'CAA': 'Q',     'AAA': 'K',     'GAA': 'E',
    'UAG': 'stop',  'CAG': 'Q',     'AAG': 'K',     'GAG': 'E',
    'UGU': 'C',     'CGU': 'R',     'AGU': 'S',     'GGU': 'G',
    'UGC': 'C',     'CGC': 'R',     'AGC': 'S',     'GGC': 'G',
    'UGA': 'stop',  'CGA': 'R',     'AGA': 'R',     'GGA': 'G',
    'UGG': 'W',     'CGG': 'R',     'AGG': 'R',     'GGG': 'G'
}

def translate_rna_to_protein(rna_string, start_pos=0):
    protein_string = ''
    for pos in range(start_pos, len(rna_string), 3):
        codon = rna_string[pos:pos+3]
        if RNA_CODON_TABLE[codon] == 'stop':
            return protein_string
        protein_string += RNA_CODON_TABLE[codon]
    return protein_string

def dna_to_rna(dna_string):
    return dna_string.replace('T', 'U') 

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



def reverse_complement(dna_string):
    rev_comp = [REV_SYMBOLS[base] for base in reversed(list(dna_string))]
    return rev_comp