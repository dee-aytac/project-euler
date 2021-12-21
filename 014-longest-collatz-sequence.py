def find_collatz():
    starting_number = -1
    chain_length = float('-inf')
    for i in range(13, 1000000):
        local_length = 0
        x = ret(i)
        while x != 1:
            local_length += 1 
            x = ret(x)
        if local_length > chain_length:
            chain_length = local_length
            starting_number = i 
    return starting_number

def ret(n):
    if n % 2 == 0: 
        return n / 2 
    else:
        return 3 * n + 1 
    

if __name__ == "__main__":
    print(find_collatz())
