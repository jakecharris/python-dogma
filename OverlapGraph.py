# Given a set of DNA sequences, return the adjacency list of the
# overlap graph for O3. That is, find pairs of DNA where the
# last 3 bases of one sequence matches the first 3 bases of another.

# Created method to quickly make FASTA dict from file
import FastaReader

def overlaps(fasta_file):
    gene_names = fastadict.gene_names(fasta_file)
    gene_seqs = fastadict.gene_seqs(fasta_file)

    # compare each gene to every other gene w/o comparing it to itself
    f = open('/Users/jakeharris/Desktop/overlaps.txt', 'x')
    gene_num = 0
    while gene_num < len(gene_seqs):
        comparisons = [j for j in range(len(gene_seqs)) if j != gene_num]  # prevents self-matching loops
        for i in comparisons:
            if gene_seqs[gene_num][-3:] == gene_seqs[i][:3]:
                overlap = gene_names[gene_num] + " " + gene_names[i] + '\n'
                f.write(overlap)
        gene_num += 1
    f.close()


if __name__ == "__main__":
    overlaps("/Users/jakeharris/Downloads/rosalind_grph.txt")