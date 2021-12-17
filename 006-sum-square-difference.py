def find_diff(n):
    sum_1 = 0
    sum_2 = ((n * (n + 1)) / 2) ** 2 
    for i in range(1, n + 1):
        sum_1 += i ** 2 
    return int(sum_2 - sum_1)

if __name__ == "__main__":
    print(find_diff(100))
