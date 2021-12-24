def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

def lattice_paths(x, y):
    return int(factorial(x + y) / (factorial(x) * factorial(y)))




if __name__ == "__main__":
    print(lattice_paths(20, 20))
