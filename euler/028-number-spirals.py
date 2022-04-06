
def number_spiral(n):
    answer = 0
    number = 1
    current_layer = 1
    while current_layer <= n:
        print(number)
        answer += number
        if number == current_layer ** 2:
            current_layer += 2
        number += (current_layer - 1)
    return answer


if __name__ == "__main__":
    print(number_spiral(1001))