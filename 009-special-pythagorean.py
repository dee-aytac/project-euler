import math
def find_special():
    for a in range(1, 1000):
        for b in range(1, 1000 - a):
            c = a ** 2 + b ** 2
            c = math.sqrt(c)
            if a + b + c == 1000:
                return (a, b, int(c))

if __name__ == "__main__":
    print(find_special())
