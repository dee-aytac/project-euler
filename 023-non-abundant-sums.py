def non_abundant_sums(n):
    abundants = []
    all_nums = [x for x in range(0, 28123)]
    for x in range(2, n):
        proper_divisors = 0
        for y in range(1, (x // 2) + 1):
            if x % y == 0:
                proper_divisors += y
        if proper_divisors > x:
            abundants.append(x)
    for i in range(len(abundants)):
        for j in range(i, len(abundants)):
            sum_ = abundants[i] + abundants[j]
            if (sum_) > 28122:
                break
            else:
                print(sum_)
                all_nums[sum_] = 0

    return all_nums
if __name__ == "__main__":
    print(sum(non_abundant_sums(28123)))