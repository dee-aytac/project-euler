import math
def find_divisors(n):
    num = -1
    start = 2
    found = False
    while not found:
        num = return_triangular(start)
        print("at", num)
        divisors = 1
        for i in range(1, int(math.sqrt(num)) + 1):
            if num % i == 0:
                divisors += 1 * 2
            if divisors > n:
                found = True
        start += 1
    return num

def return_triangular(x):
    return int(x * (x + 1) / 2)

if __name__ == "__main__":
    print(find_divisors(500))
