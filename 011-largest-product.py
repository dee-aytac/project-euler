def get_grid(file_name):
    grid = []
    for line in open(file_name):
        row = line.strip().split(' ')
        row = list(map(int, row))
        grid.append(row)
    return grid 

def find_largest_product(grid):
    rows = len(grid)
    cols = len(grid[0])
    max_product = float('-inf')
    for row in range(rows):
        for col in range(cols):
            for r, c in [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (1, 1), (1, -1), (-1, 1)]:
                or_r = r 
                or_c = c 
                local_product = 1
                for i in range(1, 5):
                    r,c = r * i, c * i 
                    rr = row + r 
                    cc = col + c 
                    r = or_r 
                    c = or_c
                    if not ((0 <= rr < rows) and (0 <= cc < cols)):
                        continue 
                    local_product = local_product * grid[rr][cc]
                max_product = max(max_product, local_product)
    return max_product

if __name__ == "__main__":
    grid = get_grid('011-input.txt')
    print(find_largest_product(grid))

