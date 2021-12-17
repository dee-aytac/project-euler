# Division method
def find_divided():
    nums = [x for x in range(2, 21)]
    sum_ = sum(x for x in nums)
    divs = []
    while sum_ != 19:
        found = False
        for num in nums:
            if found:
                break 
            for i in range(2, 21):
                if num % i == 0 and num != 0:
                    divisor = i
                    found = True 
                    break
        divs.append(divisor)
        for idx, num in enumerate(nums):
            if num % divisor == 0:
                nums[idx] = num // divisor
        sum_ = sum(x for x in nums)
        
    lcm = 1
    for idx, num in enumerate(divs):
        lcm *= num 
    return lcm



if __name__ == "__main__":
    print(find_divided())


# LCM(a,b) = (a×b)/GCF(a,b)


