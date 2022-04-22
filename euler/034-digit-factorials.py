
def digit_factorials():
    factorials = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
    answer = 0
    for i in range(10, (factorials[9] * 7)):
        local_sum = 0
        num = i
        while num > 0:
            local_sum += factorials[int(num % 10)]
            num = num // 10
        if i == local_sum:
            answer += i 
    return answer



if __name__ == "__main__":
    print(digit_factorials())