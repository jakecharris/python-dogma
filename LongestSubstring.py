# Given k num of FASTA DNA strings, find the longest common
# substring shared between all strings
import math

def longest_substring(fasta_file):
    # Create FASTA dictionary
    fasta_dict = {}
    gene_name = None
    seq_list = []  # list containing segments of genes
    with open(fasta_file, 'r') as f:
        for line in f:
            if line.startswith('>'):
                # initiates at end of gene to combine list of gene segments
                if gene_name:  # gene_name has already been made, changed from 'None'
                    fasta_dict[gene_name] = ''.join(seq_list)
                    del seq_list[:]  # empty seq_list to allow for next gene
                # create new gene_name key, redefine gene_name variable above
                gene_name = line.strip().split('>')[1]
            else:
                seq_list.append(line.strip())  # add sequence segments to list
        # meant for final gene since there is no last ">" marker
        fasta_dict[gene_name] = ''.join(seq_list)

    # find the shortest gene for comparison
    genes = list(fasta_dict.values())
    min_gene = genes[0]  # initial condition
    for i in range(len(genes)):
        if len(genes[i]) < len(min_gene):
            min_gene = genes[i]
    genes_no_min = genes
    genes_no_min.remove(min_gene)

    # search for longest segment in ever-increasing search window, starting with length 2
    i = 0
    j = 2
    search = 2  # initial segment len check
    common_substrings = []
    while j <= len(min_gene):
        substring = min_gene[i:j]
        substring_check = []
        for gene in genes_no_min:
            is_sub = substring in gene
            substring_check.append(is_sub)
        if all(substring_check):
            common_substrings.append(substring)
            i = 0
            search += 1
            j = search
            continue
        # break loop if search has reached end of gene and there are no more common substrings
        elif j == len(min_gene) and search > max(len(sub) for sub in common_substrings):
            break
        else:
            i += 1
            j += 1
        substring_check.clear()
    print(common_substrings[len(common_substrings)-1])  # yields longest string at end of list

if __name__ == '__main__':
    longest_substring('/Users/jakeharris/Downloads/rosalind_lcsm (5).txt')
    # longest_substring('/Users/jakeharris/Desktop/Untitled.txt')