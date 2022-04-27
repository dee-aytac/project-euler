from math import sqrt
from itertools import permutations

def is_prime(x):
    if x == 1:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def prime_permutations():
    for i in range(1000, 10000):
        perms = list(permutations(str(i)))
        perm_repeats = list()
        seen = set()
        for perm_tuple in perms:
            perm = "".join(perm_tuple)
            if perm[0] == '0':
                continue       
            if is_prime(int(perm)) and perm not in seen:
                seen.add(perm)
                perm_repeats.append(perm)
                if len(perm_repeats) == 3:
                    perm_repeats.sort()
                    if int(perm_repeats[1]) - int(perm_repeats[0]) == int(perm_repeats[2]) - int(perm_repeats[1]):
                        return "".join(perm_repeats)
if __name__ == "__main__":
    print(prime_permutations())