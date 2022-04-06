def find(upper_limit):
    sum_ = 0
    for i in range(upper_limit):
        if i % 3 == 0:
            print(i," % 3")
            sum_ += i 
        elif i % 5 == 0:
            print(i, " % 5")
            sum_ += i 
    return sum_

if __name__ == "__main__":
    print(find(1000))