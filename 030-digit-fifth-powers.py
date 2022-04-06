from math import sqrt

def digit_xth_powers(n):
    answer = 0
    for num in range(10, (9 ** n) * 5):
        str_num = str(num)
        local_sum = 0
        for idx in range(len(str_num)):
            local_sum += int(str_num[idx]) ** n
        if local_sum == num:
            answer += num 
    return answer

if __name__ == "__main__":
    print(digit_xth_powers(5))