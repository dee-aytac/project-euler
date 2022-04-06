import string
def score(input):
    score = 0
    alphabet = string.ascii_uppercase
    with open(input, 'r') as f:
        names = f.read().replace("\"", "").split(',')
        names.sort()
        
    for name in names:
        local_score = 0
        for char in name:
            local_score += (alphabet.index(char)) + 1
        score += (names.index(name) + 1) * local_score
    return score
if __name__ == "__main__":
    print(score("022-input.txt"))