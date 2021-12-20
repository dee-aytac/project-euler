def find_sum(fname):
    sum_ = 0
    for line in open(fname):
        sum_ += int(line)
    return str(sum_)[:10]

if __name__ == "__main__":
    print(find_sum('013-input.txt'))
