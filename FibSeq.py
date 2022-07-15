# Find the number of total rabbit pairs after n months from a beginning pair
# of rabbits which take 1 month to become old enough to reproduce and produce
# k pairs of offspring each month

def fib_rabbits(n_months, k_pairs):
    a = 0
    b = 1
    if n_months < 0:
        print('Incorrect')
    elif n_months == 0:
        return a
    elif n_months == 1:
        return b
    else:
        for i in range(1, n_months):
            total = b + k_pairs*(a)
            a = b
            b = total
        return b

if __name__ == '__main__':
    print(fib_rabbits(33, 4))
