import math 

def find_prime(n):
    start = 2
    #n -= 1
    while n > 0:
        prime = True
        for i in range(2, int(math.sqrt(start)) + 1):
            if start % i == 0:
                prime = False
                break 
        if prime:
            n -= 1 
        start += 1
    return start - 1 


if __name__ == "__main__":
    print(find_prime(10001))
