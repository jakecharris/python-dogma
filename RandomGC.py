# Given a DNA string and an array of GC-content percentages, create a new
# array of the log10 of the probability of constructing a random DNA string
# that matches the original DNA string.

import math
import numpy as np

def random_DNA_GC(dna_file):
    with open(dna_file) as f:
        dna_sample = f.readline().strip()
        gc_contents = [float(p) for p in f.readline().split()]

    # Base pair probs. based on GC content
    gc_content_probs = {}
    for i in range(len(gc_contents)):
        gc_prob = gc_contents[i] / 2
        at_prob = (1 - gc_contents[i]) / 2
        gc_content_probs[gc_contents[i]] = (gc_prob, at_prob)
    # print(gc_content_probs)

    # Calculate prob. of random string
    log10_probs = []
    for prob_value in gc_content_probs.values():
        base_probs = []
        for bp in dna_sample:
            base_probs.append(prob_value[0] if bp == 'G' or bp == 'C' else prob_value[1])
        string_product = np.prod(base_probs)
        log10_probs.append('%.3f'%math.log10(string_product))
    output = " ".join(log10_probs)
    print(output)

if __name__ == "__main__":
    random_DNA_GC("/Users/jakeharris/Downloads/rosalind_prob.txt")