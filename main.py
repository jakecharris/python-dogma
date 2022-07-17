### Python-Dogma Module ###
# functions for parsing thru molecular biology data #
import numpy as np
import regex as re
from bs4 import BeautifulSoup
from urllib.request import urlopen











# Create dict of {seq_name: sequence} from list of FASTA .txt files/URLs input
def read_sequences(seq_files, from_url=None):
    if type(seq_files) != list:
        seq_files = [seq_files]
    seq_dict = {}
    seq_name = None
    seq_list = [] 
    for file in seq_files:
        # extract FASTA seqs directly from webpages
        if from_url == True:
            url = file
            html = urlopen(url).read()
            soup = BeautifulSoup(html, features='html.parser')
            for script in soup(['script', 'style']):
                script.extract()
            f = soup.get_text().split('\n')
            seq_name = f[0].strip('>')
            seq_dict[seq_name] = ''.join(f[1:])
        # open .txt file, parse thru each line for name and sequence key:value pairs
        else:
            f = open(file, 'r')
            for line in f:
                if line.startswith('>'):
                    if seq_name:
                        seq_dict[seq_name] = ''.join(seq_list)
                        del seq_list[:]
                    seq_name = line.strip('\n').split('>')[1]
                else:
                    seq_list.append(line.strip())
            seq_dict[seq_name] = ''.join(seq_list)
    return seq_dict


# Transcribe DNA to RNA (based on coding strand)
def transcription(dna):
    rna = dna.replace('T', 'U')
    return rna


# Get reverse complement DNA string
def rev_complement(dna):
    rev_dna = dna[::-1]
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
    return rev_comp


# Find locations of motif substring within DNA/RNA/protein sequence
# **Note: returns location values of index+1 due to Python 0-indexing**
def motif_locations(sequence, motif):
    motif_locs = []
    i = 0
    seq_search = sequence[i:]
    while i < len(sequence):
        loc = seq_search.find(motif, i, len(sequence))
        if loc not in motif_locs:
            motif_locs.append(int(loc) + 1)
            i += 1
        else:
            i += 1
    motif_locs = np.unique(motif_locs)
    motif_locs = [str(m) for m in motif_locs]
    motif_locs.remove('0')
    results = " ".join(motif_locs)

    return results


if __name__ == "__main__":
    print(read_sequences("https://rest.uniprot.org/uniprotkb/P04233.fasta", from_url=True))
    fasta = ["/Users/jakeharris/Desktop/fastaex.txt", "/Users/jakeharris/Desktop/fastaex2.txt"]
    print(read_sequences(fasta))