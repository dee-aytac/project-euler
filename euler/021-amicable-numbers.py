def amicable_numbers(n):
    s = set()
    sum_of_amicables = 0
    for x in range(2, n):
        proper_divisors = 0
        for y in range(1, x):
            if x % y == 0:
                proper_divisors += y
        if ((x, proper_divisors)) in s:
            sum_of_amicables += proper_divisors + x
        s.add((proper_divisors, x))
    print(s)
    return sum_of_amicables
if __name__ == "__main__":
    print(amicable_numbers(10000))