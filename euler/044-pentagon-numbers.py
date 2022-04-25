from math import sqrt

def is_pentagonal(x):
    result = (sqrt((24*x+1)) + 1) / 6
    return result.is_integer()

def pentagon_numbers():
    k = 1
    while True:
        for j in range(1, k):
            num_j = int(j * (3*j-1) / 2)
            num_k = int(k * (3*k-1) / 2)
            if is_pentagonal(num_j + num_k) and is_pentagonal(num_k - num_j):
                return num_k - num_j
        k += 1

if __name__ == "__main__":
    print(pentagon_numbers())