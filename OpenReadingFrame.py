# Given a DNA string, give the protein output that can be translated from ORFs
# of the coding string and reverse complement string
import regex as re

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

def orf_proteins(dna_file):
    dna_segs = ""
    with open(dna_file) as f:
        for line in f.readlines()[1:]:
            dna_segs += line.strip('\n')
    dna_string = "".join(dna_segs)

    # create reverse complement of DNA string
    rev_dna = dna_string[::-1]
    rev_comp = ''
    for base in rev_dna:
        if base == 'A':
            rev_comp += 'T'
        if base == 'T':
            rev_comp += 'A'
        if base == 'G':
            rev_comp += 'C'
        if base == 'C':
            rev_comp += 'G'
    # mRNA versions
    coding_rna = dna_string.replace('T', 'U')
    rev_comp_rna = rev_comp.replace('T', 'U')

    total_orf_prot = []
    for rna in [coding_rna, rev_comp_rna]:
        # search for start/stop codon index -- have to account for different stop codons
        start_search = re.finditer("AUG", rna, overlapped=True)
        uaa_uga_search = re.finditer("U[AG]A", rna, overlapped=True)
        uag_search = re.finditer("UAG", rna, overlapped=True)
        start_i = [bp_start.start() for bp_start in start_search]
        end_j = [bp_stop.start() for bp_stop in uaa_uga_search]
        end_k = [bp_stop.start() for bp_stop in uag_search]

        # ORF pair index list based on codon length = 3
        index_list = []
        for i in start_i:
            for j in end_j:
                if j > i and ((j - i) % 3) == 0:
                    index_list.append([i, j])
            for k in end_k:
                if k > i and ((k - i) % 3) == 0:
                    index_list.append([i, k])

        # check for ORFs (start codon -> end codon)
        for pair in index_list:
            rna_segment = rna[pair[0]:pair[1]]
            orf_prot = ""
            for i in range(0, len(rna_segment), 3):
                codon = rna_segment[i:i + 3]
                orf_prot += aa_table[codon]
            total_orf_prot.append(orf_prot.split("_")[0])

    for p in set(total_orf_prot):
        print(p)


if __name__ == '__main__':
    orf_proteins('/Users/jakeharris/Downloads/rosalind_orf (2).txt')
