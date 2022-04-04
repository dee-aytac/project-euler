
def lexicographical_permutation(numbers):
    result = []
    if len(numbers) == 0:
        return []
    elif len(numbers) == 1:
        return [numbers]
    for i in range(len(numbers)):
        x = numbers[i]
        xs = numbers[:i] + numbers[i+1:]
        for perm in lexicographical_permutation(xs):
            result.append([x]+perm)
    return result


if __name__ == "__main__":
    print("".join(map(str, lexicographical_permutation([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])[999999])))