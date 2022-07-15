# Given a number of 6 couples with provided genotypes, return the average
# expected number of offspring with dominant phenotype if each couple
# has 2 offspring
# Pairings:

# 1. AA-AA    2. AA-Aa    3. AA-aa
# 4. Aa-Aa    5. Aa-aa    6. aa-aa

def avg_dominant_offspring(p1, p2, p3, p4, p5, p6):
    total_dom = 0
    total_dom += sum([p1, p2, p3])  # p1, p2, p3 all yield 100% dom phenotype
    total_dom += 0.75 * p4  # P(p4) = 75%
    total_dom += 0.5 * p5  # P(p5) = 50%
    total_dom += 0 * p6  # P(p6) = 0%
    print(2 * total_dom)  # each couple has 2 offspring

if __name__ == '__main__':
    avg_dominant_offspring(19368,19864,17474,16022,16782,18158)
    