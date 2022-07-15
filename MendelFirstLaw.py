# Given a number of organisms that are k homozygous dominant,
# m heterozygous, and n homozygous recessive, find the probability
# of 2 randomly selected organisms mating to produce an offspring with
# a dominant allele

def dom_allele_prob(k, m, n):
    total = k + m + n
    prob = (4*(k*(k-1) + 2*k*m + 2*k*n + m*n) + 3*m*(m-1)) / (4*total*(total-1))

    return prob

if __name__ == '__main__':
    print(dom_allele_prob(28, 26, 30))
