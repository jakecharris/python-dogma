# Given 2 equal length DNA strings, calculate the transition/transversion ratio
# Transition: purine-purine (A <-> G) or pyrimidine-pyrimidine (C <-> T) base change
# Transversion: purine-pyrimidine base change, less common

def trans_trnsv_ratio(fasta_file):
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
    dna1 = list(fasta_dict.values())[0]
    dna2 = list(fasta_dict.values())[1]

    # Calculate transitions, transversions
    purines = ['A', 'G']
    pyrimidines = ['C', 'T']
    transitions = 0
    transversions = 0
    for i in range(len(dna1)):
        if dna1[i] == dna2[i]:
            continue
        else:
            if dna1[i] in purines and dna2[i] in purines:
                transitions += 1
            elif dna1[i] in pyrimidines and dna2[i] in pyrimidines:
                transitions += 1
            else:
                transversions += 1
    ratio = transitions / transversions
    print(ratio)

if __name__ == "__main__":
    trans_trnsv_ratio("/Users/jakeharris/Downloads/rosalind_tran.txt")
