from doctest import OutputChecker
from Bio import Entrez, SeqIO
from Bio.Seq import translate
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

def phred(fastq):
    with open(fastq, 'r') as f:
        score = f.readline().rstrip()
        fq_records = f.readlines()
    with open('fastq_phred.txt', 'w+') as fq:
        fq.writelines(fq_records)
    below_score = 0
    for rec in SeqIO.parse('fastq_phred.txt', 'fastq'):
        phred_mean = np.mean(rec.letter_annotations['phred_quality'])
        if phred_mean < int(score):
            below_score += 1
    print(below_score)

def prot_translate(dna_file):
    with open(dna_file) as f:
        dna = f.readline().strip()
        prot = f.readline().strip()
    # print(dna.find('ATG'))
    print(len(translate(dna)), len(prot))

    

if __name__ == "__main__":
    # shortest(["FJ817486", "JX069768", "JX469983"])
    # shortest(['NM_001081821 JX445144 NM_001079732 NM_214399 NM_001185098 JX469983 JX308813 JX472277 JF927157'])
    # phred('/Users/jakeharris/Downloads/rosalind_phre.txt')
    prot_translate('/Users/jakeharris/Downloads/rosalind_ptra (1).txt')