import itertools

def pandigital_products(n):
    pandigitals = set()
    for perm in list(itertools.permutations([1, 2, 3, 4, 5, 6, 7, 8, 9])):
        n1 = perm[0] * 10 + perm[1]
        n2 = perm[2] * 100 + perm[3] * 10 + perm[4]
        n3 = perm[5] * 1000 + perm[6] * 100 + perm[7] * 10 + perm[8]
        if n1 * n2 == n3:
            pandigitals.add(n3)

        n1 = perm[0] * 100 + perm[1] * 10 + perm[2]
        n2 = perm[3] * 10 + perm[4]
        n3 = perm[5] * 1000 + perm[6] * 100 + perm[7] * 10 + perm[8]
        if n1 * n2 == n3:
            pandigitals.add(n3)

        n1 = perm[0]
        n2 = perm[1] * 1000 + perm[2] * 100 + perm[3] * 10 + perm[4]
        n3 = perm[5] * 1000 + perm[6] * 100 + perm[7] * 10 + perm[8]
        if n1 * n2 == n3:
            pandigitals.add(n3)

        n1 = perm[0] * 1000 + perm[1] * 100 + perm[2] * 10 + perm[3]
        n2 = perm[4]
        n3 = perm[5] * 1000 + perm[6] * 100 + perm[7] * 10 + perm[8]
        if n1 * n2 == n3:
            pandigitals.add(n3)

    return sum(pandigitals)

if __name__ == "__main__":
    print(pandigital_products(5))