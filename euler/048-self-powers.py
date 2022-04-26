def self_powers(n):
    total_sum = 0
    for i in range(1, n + 1):
        total_sum += i ** i
    return str(total_sum)[len(str(total_sum))-10:]

if __name__ == "__main__":
    print(self_powers(1000))