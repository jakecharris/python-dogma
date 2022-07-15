### Python-Dogma Module ###
# functions for parsing thru molecular biology data #
import numpy as np
import regex as re
from bs4 import BeautifulSoup
from urllib.request import urlopen

# Create dict of {seq_name: sequence} from FASTA text file/URL str input
def seq_dict(seq_file, from_url=None):
    seq_dict = {}
    seq_name = None
    seq_list = [] 
    # extract FASTA seqs directly from webpages
    if from_url == True:
        url = seq_file
        html = urlopen(url).read()
        soup = BeautifulSoup(html, features='html.parser')
        for script in soup(['script', 'style']):
            script.extract()
        seq_file = soup.get_text()
    # open seq_file, parse thru each line for name and sequence key:value pairs
    with open(seq_file, 'r') as f:
        for line in f:
            if line.startswith('>'):
                if seq_name:
                    seq_dict[seq_name] = ''.join(seq_list)
                    del seq_list[:]
                seq_name = line.strip().split('>')[1]
            else:
                seq_list.append(line.strip())
        seq_dict[seq_name] = ''.join(seq_list)
    return seq_dict