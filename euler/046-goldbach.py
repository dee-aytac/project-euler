from math import sqrt

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:
            return False 
    return True


def return_next_composite(n):
    n = n+1
    while True:
        for i in range(2, int(sqrt(n) + 1)):
            if n % i == 0 and n % 2 != 0:
                return n 
        n += 1


def goldbach():
    number = 9
    primes = [x for x in range(2, 10000) if is_prime(x)]
    
    while True:
        possible = False
        for prime in primes:
            if possible == True:
                break
            for square in range(1, int(sqrt(number/2)) + 1):
                if number == (prime + 2 * (square ** 2)):
                    possible = True
                    break

            if prime >= number:
                break
        if possible == False:
            return number
            
        number = return_next_composite(number)



if __name__ == "__main__":
    print(goldbach())
