#from math import sqrt
# def distinct_powers(n): # Tried to use the short way but its somehow off by one when n = 100
#     numbers = ((n - 2) + 1) * ((n - 2) + 1)
#     powers = list()
#     repeat = 0
    
#     for i in range(2, n):
#         k = 2
#         while True:
#             x = i ** k
#             if x > n:
#                 break
#             powers.append((i, k))
#             k += 1
#     for base in powers:
#         local_repeat = 0
#         for i in range(2 * base[1], n + 1, base[1]):
#             #print(base[0], base[1], i)
#             local_repeat += 1
#         print(base[0], base[1], local_repeat)
#         repeat += local_repeat
#     print(((n - 2) + 1) * (n))
#     return powers, numbers - (repeat)

def distinct_powers(n):
    distinct_numbers = set()
    for a in range(2, n + 1):
        for b in range(2, n + 1):
            distinct_numbers.add(a**b)
    return len(distinct_numbers)

if __name__ == "__main__":
    print(distinct_powers(100))