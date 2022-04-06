import math
def find_primes(n):
    sum_of_primes = 0
    start = 2
    while start < n:
        print(start)
        prime = True
        for i in range(2, int(math.sqrt(start)) + 1):
            if start % i == 0: 
                prime = False 
                break 
        if prime:
            print(start, "is prime")
            sum_of_primes += start 
        start += 1
    
    return sum_of_primes

if __name__ == "__main__":
    print(find_primes(2000000))


