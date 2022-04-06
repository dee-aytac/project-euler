def fibonacci(idx, n1, n2):
    return (idx + 1, n2, n1+n2)

def find_n_digit(n):
    i = 1
    n1 = 0
    n2 = 1
    while True:
        i, n1, n2 = fibonacci(i, n1, n2)
        if len(str(n2)) >= n:
            break
    return i
if __name__ == "__main__":
    print(find_n_digit(1000))