# Calculate the GC content levels of given FASTA sequence and
# display the one with the highest GC level

def highest_gc_content(fasta_file):

    # Create FASTA dictionary
    fasta_dict = {}
    header = None
    seq_list = []
    with open(fasta_file, 'r') as f:
        for line in f:
            if line.startswith('>'):    # define headers for each gene
                if header:  # <- 'None' means that make k:v for new gene
                    fasta_dict[header] = ''.join(seq_list)   # gene header: joined segments within seq_list
                    del seq_list[:]   # empty the seq_list to allow for next gene
                header = line.strip().split('>')[1]  # create new dict key for gene name
            else:
                seq_list.append(line.strip())  # add sequence segments to list
        # meant for final gene since there is no last ">" marker
        fasta_dict[header] = ''.join(seq_list)

    # Find gene with highest GC content
    highest_gc_gene = ''
    highest_gc_content = 0
    for (header, seq) in fasta_dict.items():
        gc_content = round(((seq.count('G') + seq.count('C')) / len(seq) * 100), 4)
        if gc_content > highest_gc_content:
            highest_gc_gene = header
            highest_gc_content = gc_content
        else:
            continue
    return highest_gc_gene, highest_gc_content


if __name__ == '__main__':
    print(highest_gc_content('/Users/jakeharris/Downloads/rosalind_gc.txt'))
