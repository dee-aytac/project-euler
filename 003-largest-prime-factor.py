def find_primes(n):
    d = 2
    while True:
        while n % d == 0:
            print("Really?", n, "to", d, n / d)
            n = n / d
        d += 1
        if d * d > n:
            print("d * d is", d * d)
            print("New max is", n)
            max_ = n
            break
    return max_


if __name__ == "__main__":
    print(find_primes(600851475143))
    
