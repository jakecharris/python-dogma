# Transcribe a string of DNA into its corresponding RNA string (replace 'T' for 'U')

def dna_to_rna(dna_file):

    with open(dna_file, 'r') as f:
        dna = f.read()

    rna = dna.replace('T', 'U')
    print(rna)

    return rna

if __name__ == '__main__':
    dna_to_rna('/Users/jakeharris/Downloads/rosalind_rna (1).txt')

