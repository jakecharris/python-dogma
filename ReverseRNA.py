# Given a protein string, try to infer the number of possible
# different mRNA sequences based on the amino acids modulo 1000000
# **Remember the STOP codon at the end**

def rev_translate(protein_file):
    with open(protein_file) as f:
        protein = f.read().strip()
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

    # Make dict of count of codons for each amino acid
    codon_count = {}
    for (codon, aa) in aa_table.items():
        codon_count[aa] = sum([1 for i in aa_table.values() if i == aa])

    # Calculate possible combinations of codons based on amino acid string
    mrna_combs = 1
    for aa in protein:
        mrna_combs *= codon_count[aa]
    mrna_combs *= 3  # STOP codon possibilities

    print(mrna_combs % 1000000) # mod 1000000

if __name__ == '__main__':
    rev_translate('/Users/jakeharris/Downloads/rosalind_mrna.txt')