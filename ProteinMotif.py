# Given list of 15 UniProt database access IDs, find the locations of the
# N-glycosylation motif in each protein (if present).
# Note: the problem wants locations, meaning index+1 due to Python's 0-indexing
# N-glycosylation motif: N{P}[ST]{P}
#   - {X}: any a.a. except for X
#   - [XY]: either X or Y

from bs4 import BeautifulSoup
from urllib import request
import regex as re  # use 3rd-party regex package for overlapping index locations

def protein_motif(uniprot_file):
    # Open the Uniprot FASTA page to parse thru each protein seq
    prot_dict = {}
    with open(uniprot_file) as f:
        for id in f.readlines():
            uniprot_id = id.strip()
            uniprot_url = f'https://www.uniprot.org/uniprot/{uniprot_id}.fasta'
            prot_html = request.urlopen(uniprot_url)
            soup = BeautifulSoup(prot_html, 'html.parser')
            fasta_text = soup.get_text()
            no_header = fasta_text.split('\n')[1:]  # remove FASTA header
            prot_seq = ''.join(no_header)
            prot_dict[uniprot_id] = prot_seq

    # Search for N{P}[ST]{P} motif in each protein
    for id in prot_dict.keys():
        index = []
        motif_search = re.findall("N[^P][ST][^P]", prot_dict[id], overlapped=True)
        # r"(?=(N[^P][ST][^P]))" for normal overlaps in re, overlapped=True for regex package
        for motif in motif_search:
            index.append(str(prot_dict[id].find(motif) + 1))
        if len(index) > 0:
            print(id)
            print(' '.join(index))
        else:
            continue

if __name__ == '__main__':
    protein_motif('/Users/jakeharris/Downloads/rosalind_mprt.txt')