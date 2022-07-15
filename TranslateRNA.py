# Translate an mRNA string into a protein string based on codons

def mrna_translation(rna_file):
    with open(rna_file, 'r') as f:
        seq_list = []
        for line in f:
            seq_list.append(line.strip())
        mrna = ''.join(seq_list)

    aa_table = {'UUU': 'F', 'CUU': 'L', 'AUU': 'I', 'GUU': 'V',
                'UUC': 'F', 'CUC': 'L', 'AUC': 'I', 'GUC': 'V',
                'UUA': 'L', 'CUA': 'L', 'AUA': 'I', 'GUA': 'V',
                'UUG': 'L', 'CUG': 'L', 'AUG': 'M', 'GUG': 'V',
                'UCU': 'S', 'CCU': 'P', 'ACU': 'T', 'GCU': 'A',
                'UCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A',
                'UCA': 'S', 'CCA': 'P', 'ACA': 'T', 'GCA': 'A',
                'UCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A',
                'UAU': 'Y', 'CAU': 'H', 'AAU': 'N', 'GAU': 'D',
                'UAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D',
                'UAA': '_', 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E',
                'UAG': '_', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E',
                'UGU': 'C', 'CGU': 'R', 'AGU': 'S', 'GGU': 'G',
                'UGC': 'C', 'CGC': 'R', 'AGC': 'S', 'GGC': 'G',
                'UGA': '_', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G',
                'UGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G'}

    protein = ''
    start = mrna.find('AUG')
    for i in range(start, len(mrna), 3):
        codon = mrna[i:3+i]
        if codon == 'UAG' or codon == 'UAA' or codon == 'UGA':
            break
        else:
            protein += aa_table[codon]

    return protein


if __name__ == '__main__':
    print(mrna_translation('/Users/jakeharris/Downloads/rosalind_prot.txt'))

