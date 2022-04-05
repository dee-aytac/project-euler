from math import sqrt

def funct(a, b, n):
    return (n ** 2) + (a * n) + b

def is_prime(n):
    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:
            return False 
    return True

def quadratic_primes(a, b):
    max_primes = -1
    product_of_coef = -1
    for i in range(-a, a):
        for j in range(-b, b + 1):
            local_prime = 0
            for n in range(0, 100):
                value = funct(i, j, n)
                if value < 0:
                    break
                if is_prime(value):
                    local_prime += 1
                else:
                    break
            if local_prime > max_primes:
                max_primes = local_prime
                product_of_coef = i * j
    return product_of_coef
if __name__ == "__main__":
    print(quadratic_primes(1000, 1000))