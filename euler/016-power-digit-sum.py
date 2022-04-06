def find_digit(n):
    s = 2 ** n
    s = str(s)
    sum_ = 0 
    for char in s:
        sum_ += int(char)
    return sum_

if __name__ == "__main__":
    print(find_digit(1000))
