# Find the indeces of the individual bases of a subsequence motif within
# a DNA string. They do not have to be contiguous.
# Note: due to Python 0-indexing, return indeces + 1

def spliced_motif(fasta_file):
    fasta_dict = {}
    gene_name = None
    seq_list = []  # list containing segments of genes
    with open(fasta_file, 'r') as f:
        for line in f:
            if line.startswith('>'):
                if gene_name:
                    fasta_dict[gene_name] = ''.join(seq_list)
                    del seq_list[:]
                gene_name = line.strip().split('>')[1]
            else:
                seq_list.append(line.strip())
        fasta_dict[gene_name] = ''.join(seq_list)
    full_dna = list(fasta_dict.values())[0]
    subseq = list(fasta_dict.values())[1]

    # Search for indeces of subseq bases within full_dna
    index_locs = []
    i = 0
    j = 0
    while i < len(full_dna) and j < len(subseq):
        if full_dna[i] == subseq[j]:
            index_locs.append(i+1)
            j += 1
        else:
            pass
        i += 1
    txt_locs = " ".join(str(i) for i in index_locs)
    print(txt_locs)

if __name__ == '__main__':
    print(spliced_motif('/Users/jakeharris/Downloads/rosalind_sseq.txt'))
