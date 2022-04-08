
#1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
def coin_sum(coins, target):
    possible_ways = [0 for _ in range(target + 1)]
    possible_ways[0] = 1
    for i in range(0, len(coins)):
        for j in range(coins[i], target + 1):
            possible_ways[j] += possible_ways[j-coins[i]]
    return possible_ways[target]



if __name__ == "__main__":
    print(coin_sum([1, 2, 5, 10, 20, 50, 100, 200], 200))