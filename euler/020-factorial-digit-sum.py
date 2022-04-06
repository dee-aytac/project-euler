def find_digit_sum(n):
    product = 1 
    for i in range(1, n + 1):
        product *= i
    sum_ = 0
    for digit in str(product):
        sum_ += int(digit)
    return sum_


if __name__ == "__main__":
    print(find_digit_sum(100))
