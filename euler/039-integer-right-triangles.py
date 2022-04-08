
def integer_right_triangles(n):
    special_triangles = [[3, 4, 5], [5, 12, 13], [8, 15, 17], [7, 24, 25]] # 12, 30, 40, 56
    max_solution = -1
    answer = -1
    for i in range(3, n):
        local_solution = 0
        for triangle in special_triangles:
            if i % sum(triangle) == 0:
                for j in range(1, i // sum(triangle) + 1):
                    if i == sum(triangle) * j:
                        print(triangle[0]*j, triangle[1]*j, triangle[2]*j, "-", i)
                        local_solution += 1

        if local_solution > max_solution:
            max_solution = local_solution
            answer = i
    return answer

if __name__ == "__main__":
    print(integer_right_triangles(1000))