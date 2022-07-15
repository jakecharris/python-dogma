# For 2 DNA strings, find the longest common substring between them
# while accounting for non-continuous sequencing due to intron splicing.
# Example:
# Rosalind_23       Rosalind_64         Answer
# AACCTTGG          ACACTGTGA           AACTGG

import FastaReader as fr

def splicedSubstring(fasta_file):
    # Load in FASTA sequences
    gene1 = fr.gene_seqs(fasta_file)[0]
    print(len(gene1))
    gene2 = fr.gene_seqs(fasta_file)[1]
    print(len(gene2))

    # Iterate thru each bp in genes to check for matches
    answer = ''  # placeholder for bp answer
    i = 0
    j = 0
    while i < len(gene1):
        try:
            if gene1[i] == gene2[j] and j < len(gene2):  # check for bp match and length
                print(f"MATCH i={i}, j={j}: {gene1[i]}")  # if match found...
                answer += gene1[i]
                i += 1  # ...move index in both genes
                j += 1
            elif gene1[i] != gene2[j] and j < len(gene2):  # if no match...
                # print(f"i={i}, j={j}")
                j += 1  # ...move on in gene2
        except IndexError:  # if end of gene2 is reached
            print("LIMIT")
            break
            # i += 1
            # j = j - i  # reset to smaller index

    print(f"Output: {answer}")
    with open('/Users/jakeharris/Desktop/splice.txt', 'w') as f:
        f.write(answer)


if __name__ == "__main__":
    splicedSubstring("/Users/jakeharris/Downloads/rosalind_lcsq (2).txt")