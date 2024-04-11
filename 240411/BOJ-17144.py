import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
direction_up = [[0,1], [-1,0], [0,-1], [1,0]]
direction_down = [[0,1], [1,0], [0,-1], [-1,0]]

R, C, T = map(int, input().split())
matrix = []
for _ in range(R):
    matrix.append([int(num) for num in input().split()])

top = 0
bottom = 0
for i in range(R):
    if matrix[i][0] == -1:
        if top == 0:
            top = i
            bottom = i+1
            break

for _ in range(T):
    tmp_arr = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if matrix[i][j] != 0 and matrix[i][j] != -1:
                tmp = 0
                for k in range(4):
                    nx = dx[k] + i
                    ny = dy[k] + j
                    if 0 <= nx < R and 0 <= ny < C and matrix[nx][ny] != -1:
                        tmp_arr[nx][ny] += matrix[i][j] // 5
                        tmp += matrix[i][j] // 5
                matrix[i][j] -= tmp

    for i in range(R):
        for j in range(C):
            matrix[i][j] += tmp_arr[i][j]
    
    direct = 0
    tmp = 0
    x, y = top, 1
    while True:
        nx = x + direction_up[direct][0]
        ny = y + direction_up[direct][1]
        if x == top and y == 0:
            break
        if nx < 0 or nx>=R or ny<0 or ny>=C:
            direct += 1
            continue
        matrix[x][y], tmp = tmp, matrix[x][y]
        x = nx
        y = ny
    
    direct = 0
    tmp = 0
    x, y = bottom, 1
    while True:
        nx = x + direction_down[direct][0]
        ny = y + direction_down[direct][1]
        if x == bottom and y == 0:
            break
        if nx < 0 or nx>=R or ny<0 or ny>=C:
            direct += 1
            continue
        matrix[x][y], tmp = tmp, matrix[x][y]
        x = nx
        y = ny

answer = 0
for r in range(R):
    for c in range(C):
        if matrix[r][c] > 0:
            answer += matrix[r][c]
print(answer)