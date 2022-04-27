from math import sqrt
from itertools import permutations


def get_prime_factors(number):
    factors = set()
    divisor = 2
    while number != 1:
        if number % divisor == 0:
            factors.add(divisor)
            number = number / divisor  
        else:
            divisor += 1
    return factors


def distinct_prime_factors(start):
    number = start
    con = 0
    while True:
        print(number)
        prime_factors = get_prime_factors(number)
        if len(prime_factors) == 4:
            con += 1
            if con == 4:
                return(number - 3)
        else:
            con = 0
        number += 1
if __name__ == "__main__":
    print(distinct_prime_factors(646))
    #print(prime_factors(646))