import sys
input = sys.stdin.readline

matrix = [[0]*101 for _ in range(101)]
direction_mode = [[1, 0], [0, -1], [-1, 0], [0, 1]]
N = int(input())
for _ in range(N):
    x, y, d, g = map(int, input().split())
    matrix[x][y] = 1
    nx = x + direction_mode[d][0]
    ny = y + direction_mode[d][1]
    matrix[nx][ny] = 1

    direction = [d]
    for _ in range(g):
        temp_direction = []
        for index in range(len(direction) - 1, -1, -1):
            nd = (direction[index] + 1) % 4
            temp_direction.append(nd)

            nx = nx + direction_mode[nd][0]
            ny = ny + direction_mode[nd][1]
            matrix[nx][ny] = 1
        direction += temp_direction

answer = 0
for r in range(100):
    for c in range(100):
        if matrix[r][c] == 1 and matrix[r+1][c] == 1 and matrix[r][c+1] == 1 and matrix[r+1][c+1] == 1:
            answer += 1
print(answer)