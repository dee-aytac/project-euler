from fractions import Fraction
def dcf():
    product = 1
    for i in range(10, 100):
        for j in range(10, 100):
            if i % 10 == 0 or j % 10 == 0:
                continue
            simple = -1
            n = str(i)
            d = str(j)
            if n[0] in d:
                simple = int(n[1]) / int(d[1-d.index(n[0])])
            elif n[1] in d:
                simple = int(n[0]) / int(d[1-d.index(n[1])])
            if simple > 0.99:
                continue
            if simple == i / j:
                product *= simple
    return Fraction(product).limit_denominator()
if __name__ == "__main__":
    print(dcf())