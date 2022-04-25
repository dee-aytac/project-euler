from itertools import permutations

def sub_divisibility():
    total_sum = 0
    divisors = [2, 3, 5, 7, 11, 13, 17]
    numbers = list(permutations(range(0, 10)))
    for num in numbers:
        if num[0] == 0:
            continue
        divisible = True
        for idx, divisor in zip(range(1, 8), divisors):
            local_sum = num[idx] * 100 + num[idx+1] * 10 + num[idx+2]
            if local_sum % divisor != 0:
                divisible = False
                break
        if divisible:
            str_num = [str(integer) for integer in num]
            total_sum += int("".join(str_num))

    return total_sum

if __name__ == "__main__":
    print(sub_divisibility())