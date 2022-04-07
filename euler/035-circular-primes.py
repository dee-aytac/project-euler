from math import sqrt

def rotate_left_by_one(string):
    return string[1:] + string[0:1]

def is_prime(n):
    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:
            return False 
    return True

def circular_primes(n):
    answer = list()
    for num in range(2, n):
        if is_prime(num):
            circular = True
            str_num = str(num)
            for i in range(len(str_num) - 1):
                str_num = rotate_left_by_one(str_num)
                if not is_prime(int(str_num)):
                    circular = False
                    break
            if circular:
                answer.append(num)
    return len(answer)

if __name__ == "__main__":
    print(circular_primes(1000000))