from math import sqrt

def is_prime(x):
    if x == 1:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def prime_sum(n):
    
    i = 2
    primes_bellow_1m = list()
    while True:
        if is_prime(i):
            if sum(primes_bellow_1m) + i > 1_000_000:
                break
            else:
                primes_bellow_1m.append(i)
        i += 1
    s = set(primes_bellow_1m)
    longest_prime_len = 0
    new_sum = 0
    for i in range(-1, len(primes_bellow_1m)):
        print(i, len(s))
        new_list = []
        for j in range(i + 1, len(primes_bellow_1m)):
            new_list.append(primes_bellow_1m[j])
            local_sum = sum(new_list)
            if is_prime(local_sum):
                if len(new_list) > longest_prime_len:
                    longest_prime_len = len(new_list)
                    new_sum = local_sum
    return new_sum

if __name__ == "__main__":
    print(prime_sum(1000))