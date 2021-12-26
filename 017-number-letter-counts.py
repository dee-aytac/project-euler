
ones_ = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
"sixteen", "seventeen", "eighteen", "nineteen", "twenty", ""]

tens_ = ["ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety", ""] 


def ones(x):
    return ones_[x - 1]

def ten(x):
    return ones_[x - 1]
    
def tens(x):
    return tens_[(x % 10) - 1]

def hundreds(x):
    if ones_[x - 1]:
        return ones_[x - 1] + "hundret"
    return ""
def thousands(x):
    return ones_[x - 1] + "thousand"

def count(n):
    sum_ = 0
    for i in range(1, n + 1):
        s = ""
        char = str(i)
        #print(char)
        if len(char) == 4:
            s += thousands(int(char[0]))
            char = char[1:]
        if len(char) == 3:
            s += hundreds(int(char[0]))
            char = char[1:]
            if str(i)[-1] != "0" or str(i)[-2] != "0":
                s += "and"
        if len(char) == 2:
            if char[0] == "1":
                s += ten(int(char))
            else:
                s += tens(int(char[0]))
                char = char[1:] 
        if len(char) == 1:
            s += ones(int(char))
        sum_ += len(s) 
    return sum_


if __name__ == "__main__":
    print(count(1000))

