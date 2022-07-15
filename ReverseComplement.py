# Given a DNA string, find its reverse complement (reverse of the string and then its complementing bases)

def rev_complement(dna_file):
    with open(dna_file, 'r') as f:
        dna = f.read()

    rev_dna = dna[::-1]
    rev_comp = ''

    for base in rev_dna:
        if base == 'A':
            rev_comp = rev_comp + 'T'
        if base == 'T':
            rev_comp = rev_comp + 'A'
        if base == 'G':
            rev_comp = rev_comp + 'C'
        if base == 'C':
            rev_comp = rev_comp + 'G'

    return rev_comp

if __name__ == '__main__':
    print(rev_complement('/Users/jakeharris/Downloads/rosalind_revc (1).txt'))