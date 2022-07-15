# Module for creating dict of {gene_name: seq} from FASTA file


def fasta_dict(fasta_file):
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
    return fasta_dict

def gene_names(fasta_file):
    return list(fasta_dict(fasta_file).keys())

def gene_seqs(fasta_file):
    return list(fasta_dict(fasta_file).values())