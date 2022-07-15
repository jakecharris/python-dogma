# Given a DNA string and subsequent intron sequences, transcribe and translate
# the remaining exon sequences into a protein.
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

def rna_splicing(fasta_file):
    # Create FASTA dictionary
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
    introns = list(fasta_dict.values())[1:]

    # remove introns from full_dna, transcribe DNA -> mRNA
    edit_dna = full_dna
    for i in introns:
        edit_dna = edit_dna.replace(i, '')
    mrna = edit_dna.replace('T', 'U')
    # print(mrna)

    # translate mRNA -> protein
    # search for start/stop codon index -- have to account for different stop codons
    start_search = re.finditer("AUG", mrna, overlapped=True)
    uaa_uga_search = re.finditer("U[AG]A", mrna, overlapped=True)
    uag_search = re.finditer("UAG", mrna, overlapped=True)
    start_i = [bp_start.start() for bp_start in start_search]
    end_j = [bp_stop.start() for bp_stop in uaa_uga_search]
    end_k = [bp_stop.start() for bp_stop in uag_search]

    # ORF pair index list based on codon length = 3
    index_list = []
    total_orf_prot = []
    for i in start_i:
        for j in end_j:
            if j > i and ((j - i) % 3) == 0:
                index_list.append([i, j])
        for k in end_k:
            if k > i and ((k - i) % 3) == 0:
                index_list.append([i, k])

    for pair in index_list:
        rna_segment = mrna[pair[0]:pair[1]]
        orf_prot = ""
        for i in range(0, len(rna_segment), 3):
            codon = rna_segment[i:i + 3]
            orf_prot += aa_table[codon]
        total_orf_prot.append(orf_prot.split("_")[0])
    uniq_prot = list(set(total_orf_prot))
    print(sorted(uniq_prot, key=len)[-1])

if __name__ == "__main__":
    rna_splicing("/Users/jakeharris/Downloads/rosalind_splc (1).txt")