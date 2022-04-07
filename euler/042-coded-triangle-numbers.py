import string

def coded_triangle_numbers(fname):
    alphabet = string.ascii_uppercase
    triangle_words = 0
    triangle_numbers = list()
    n = 1

    with open(fname, 'r') as f:
        content = f.read().split(',')
    longest_list = max(content, key=len)
    upper_limit = len(longest_list) * (len(alphabet) + 1)
    
    while True:
        num = int((n + 1) * (0.5 * n))
        if num > upper_limit:
            break
        n += 1
        triangle_numbers.append(num)

    for word in content:
        word_value = 0
        word = word.replace("\"", "")
        for char in word:
            word_value += (alphabet.index(char) + 1)
        if word_value in triangle_numbers:
            triangle_words += 1

    return triangle_words

if __name__ == "__main__":
    print(coded_triangle_numbers("042-input.txt"))