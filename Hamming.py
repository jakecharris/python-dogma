# Given 2 DNA strings of equal length, find their Hamming distance
# i.e. the number of base differences between them

def hamming(dna_file):
    with open(dna_file, 'r') as f:
        dna1 = f.readline().strip()
        dna2 = f.readline().strip()

    hamming_dist = 0
    for i in range(len(dna1)):
        if dna1[i] != dna2[i]:
            hamming_dist += 1

    return hamming_dist

if __name__ == '__main__':
    print(hamming('/Users/jakeharris/Downloads/rosalind_hamm.txt'))