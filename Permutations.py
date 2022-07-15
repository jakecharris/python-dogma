# Given an integer n, find the total number of permutations of length n and
# a list of all the permutations

from itertools import permutations
import math
import numpy as np
np.set_printoptions(threshold=np.inf)

n = 5
fact = math.factorial(n)
print(fact)

nums = range(1, n+1)
perms = [list(x) for x in list(permutations(nums))]
# print(perms)
perm_array = np.array(perms)
perm_array = str(perm_array)
total_perms = perm_array.replace(" [", "").replace('[', '').replace(']', '')

with open('/Users/jakeharris/Desktop/perm_nums.txt', 'w') as f:
    f.write(str(fact))
    f.write('\n')
    f.write(total_perms)