def fibonacci(n):
    if n <= 1:
       return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def find_even_sum(upper_limit):
    sum_ = 0
    even_sum = 0
    i = 2
    while True:
        ans = fibonacci(i)
        if ans % 2 == 0:
            even_sum += ans
        if sum_ >= upper_limit:
            break
        sum_ += ans
        i += 1
    return even_sum
if __name__ == "__main__":
    print(find_even_sum(4000000))