def cycles(d):
    answer = -1
    length_of_longest_cycle = -1
    for i in range(2, d):
        value = 1
        remainders = []
        while True:
            remaining = value % i
            if remaining in remainders:
                length_of_recurring = len(remainders) - remainders.index(remaining)
                if length_of_recurring > length_of_longest_cycle: 
                    length_of_longest_cycle = length_of_recurring
                    answer = i
                break
            value = remaining * 10
            remainders.append(remaining)

    return answer


if __name__ == "__main__":
    print(cycles(1000))