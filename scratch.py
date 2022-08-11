from doctest import OutputChecker
from Bio import Entrez, SeqIO
import numpy as np
Entrez.email = 'jakec.harris@gmail.com'
# handle = Entrez.esearch(db='nucleotide', term='"Dascyllus"[Organism] AND ("2000/04/06"[PDAT] : "2011/03/22"[PDAT])')
# record = Entrez.read(handle)
# print(record['Count'])


def shortest(ids):
    handle = Entrez.efetch(db='nucleotide', id=ids[0].split(), rettype='fasta', retmode='text')
    records = list(SeqIO.parse(handle, 'fasta'))
    handle.close()

    i = 1
    short_desc = records[0].description
    short_seq = records[0].seq
    while i < len(ids):
        if len(records[i].seq) < len(short_seq):
            short_desc = records[i].description
            short_seq = records[i].seq
        i += 1
    
    print('>' + short_desc + '\n' + short_seq)

def fizzbuzz():
    for i in range(1, 101):
        fizz = "Fizz" if i%3 == 0 else ''
        buzz = 'Buzz' if i%5 == 0 else ''
        print(f'{fizz}{buzz}' or i)

def fastaq_conv(fastq):
    records = SeqIO.parse(fastq, 'fastq')
    output_file = '/Users/jakeharris/Desktop/conv.fasta'
    SeqIO.write(records, output_file, 'fasta')
    with open(output_file) as fasta_record:
        fasta_record = list(SeqIO.parse(output_file, 'fasta'))
        for record in fasta_record:
            # print(record.id, record.seq)
            print(SeqIO.FastaIO.as_fasta_2line(record))

if __name__ == "__main__":
    # shortest(["FJ817486", "JX069768", "JX469983"])
    # shortest(['NM_001081821 JX445144 NM_001079732 NM_214399 NM_001185098 JX469983 JX308813 JX472277 JF927157'])
    fastaq_conv('/Users/jakeharris/Downloads/rosalind_tfsq.txt')