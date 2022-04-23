from math import sqrt

def is_pandigital(number):
    str_num = str(number)
    for i in range(1, 8):
        if not(str(i) in str_num):
            return False 
    return True

def is_prime(n):
    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:
            return False 
    return True

def pandigital_prime(upper_limit):
    for num in range(upper_limit, 1234567, -1):
        if is_pandigital(num):
            if is_prime(num):
                return num



if __name__ == "__main__":
    print(pandigital_prime(9999999)) # I tried 7-digit since sums of 1..8 and 1..9 are 36 & 45 respectively