def find_max_sum(fname):
    n = list()
    for row in open(fname):
        numbers = row.strip().split(' ')
        numbers = list(map(int, numbers))
        n.append(numbers)

    for i in range(len(n) - 2, -1, -1):
        for j in range(len(n[i])):
            n[i][j] = n[i][j] + max(n[i + 1][j], n[i + 1][j + 1])
        n.pop()
    return n[0][0]
if __name__ == "__main__":
    print(find_max_sum('018-input.txt'))