# Given an RNA string, find the number of possible perfect combinations
# of perfect matches for a secondary RNA hairpin structure using base pairing.

import FastaReader
from math import factorial

def perfect_matches(fasta_file):
    rna = fastadict.gene_seqs(fasta_file)[0]
    # separate perfect matchings of AU and GC pairs, then multiply factorials
    AU = 0
    GC = 0
    for i in rna:
        if i == 'A':  # only need to +1 for pair
            AU += 1
        elif i == 'G':
            GC += 1
    matches = factorial(AU) * factorial(GC)
    print(matches)

if __name__ == "__main__":
    perfect_matches("/Users/jakeharris/Downloads/rosalind_pmch.txt")

