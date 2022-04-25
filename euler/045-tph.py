from math import sqrt

def is_pentagonal(x):
    result = (sqrt((24*x+1)) + 1) / 6
    return result.is_integer()

def hexagonal(x): # no need to calculate triangulars since hexagonal numbers are a subset of triangular numbers
    return int(x*(2*x-1))

def tph():
    i = 144
    while True:
        number = hexagonal(i)
        if is_pentagonal(number):
            return number
        i += 1
if __name__ == "__main__":
    print(tph())