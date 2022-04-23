def constant():
    desired_digit = 1
    num = 0
    index = 0
    product = 1
    while desired_digit <= 1000000:
        num += 1
        for char in str(num):
            index += 1
            if index == desired_digit:
                product *= int(char)
                desired_digit *= 10

    return product


if __name__ == "__main__":
    print(constant())