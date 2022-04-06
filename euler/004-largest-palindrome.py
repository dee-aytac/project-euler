def find_palindrome():
    palindrome = float('-inf')
    for n in range(100, 1000):
        for n2 in range(100, 1000):
            num = n * n2
            num = str(num)
            length_ = len(num)
            if num == num[::-1]:
                palindrome = max(int(num), palindrome)
    return palindrome 

if __name__ == "__main__":
    print(find_palindrome())
    
