from math import sqrt

def left_prime(num):
    len_s = len(str(num))
    mod = 10 ** (len_s - 1)
    for _ in range(len_s - 1):
        num = num % mod
        mod = mod / 10
        if not is_prime(num):
            return False 
    return True 


def right_prime(num):
    len_s = len(str(num))
    for _ in range(len_s - 1):
        num = num // 10
        if not is_prime(num):
            return False 
    return True 

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:
            return False 
    return True

def truncatable_primes(n):
    answer = 0
    number = 11
    count = 0
    while count < 11:
        if is_prime(number):
            if left_prime(number) and right_prime(number):
                answer += number
                count += 1
        number += 1

    return answer

if __name__ == "__main__":
    print(truncatable_primes(1000000))