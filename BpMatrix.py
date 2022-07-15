# Given a collection of FASTA strings, return a profile matrix of the number of times
# each bp occurs between them and a consensus DNA string based on the most common bp
# for each matrix column

# DNA matrix: m rows (num of FASTA inputs) x n columns (len of each input string)

import numpy as np

def consensus(fasta_file):
    # Create matrix of input fasta DNA sequences
    fasta_dna = []
    gene_seqs = []
    with open(fasta_file, 'r') as f:
        for line in f.readlines():
            if line.startswith('>'):
                gene = ''.join(gene_seqs)
                fasta_dna.append(gene)
                del gene_seqs[:]
            else:
                gene_seqs.append(line.strip())
        gene = ''.join(gene_seqs)
        fasta_dna.append(gene)
        fasta_dna.remove('')  # remove remaining blank
    dna_matrix = np.asmatrix([list(fasta_dna[i]) for i in range(len(fasta_dna))])
    print(dna_matrix)

    # Create matrix of total count of each aligned bp
    bp_count = np.zeros([4, len(fasta_dna[0])])
    for j in range(len(fasta_dna[0])):
        bp_count[0, j] = sum(1 for i in range(10) if dna_matrix[i,j] == 'A')
        bp_count[1, j] = sum(1 for i in range(10) if dna_matrix[i,j] == 'G')
        bp_count[2, j] = sum(1 for i in range(10) if dna_matrix[i,j] == 'C')
        bp_count[3, j] = sum(1 for i in range(10) if dna_matrix[i,j] == 'T')
    bp_count = bp_count.astype(int)
    print(bp_count)

    # Determine consensus DNA based on most common bp at each location
    cons_dna = []
    for i in range(bp_count.shape[1]):
        if np.argmax(bp_count[:,i], axis=0) == 0:
            cons_dna.append('A')
        elif np.argmax(bp_count[:,i], axis=0) == 1:
            cons_dna.append('G')
        elif np.argmax(bp_count[:,i], axis=0) == 2:
            cons_dna.append('C')
        elif np.argmax(bp_count[:,i], axis=0) == 3:
            cons_dna.append('T')
    print(''.join(cons_dna))

if __name__ == '__main__':
    consensus('/Users/jakeharris/Downloads/rosalind_cons (1).txt')