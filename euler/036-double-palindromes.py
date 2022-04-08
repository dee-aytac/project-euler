
def palindrome(s):
    return s == s[::-1]

def double_base_palindromes(n):
    answer = 0
    for num in range(1, n):
        if palindrome(str(num)) and palindrome(str(format(num, "b"))):
            answer += num
            print(num)
    return answer

if __name__ == "__main__":
    print(double_base_palindromes(1000000))