def find_product(fname):
    with open(fname, 'r') as f:
        content = f.read()
    s = content.replace('\n', '')
    max_product = float('-inf')
    for idx in range(len(s) - 13):
        product = 1 
        for i in range(0, 13):
            product *= int(s[idx + i])
        max_product = max(max_product, product)
    print(max_product)
if __name__ == "__main__":
    find_product('008-input.txt')
