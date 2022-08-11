# Given a string of DNA bases, return the numbers of A, C, G, T bases, respectively

def count_dna_bases(dna_file):

    with open(dna_file, 'r') as f:
        dna = f.read()

    base_counts = {'A':0, 'C':0, 'G':0, 'T':0}
    for base in base_counts.keys():
        base_counts[base] = dna.count(base)

    # for k,count in base_counts.items():
    #     print(count)

    # return count
    print(base_counts) 

if __name__ == '__main__':
    count_dna_bases('/Users/jakeharris/Downloads/rosalind_ini.txt')