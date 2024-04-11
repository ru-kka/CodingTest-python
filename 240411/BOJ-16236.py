from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

N = int(input())
matrix = []
for _ in range(N):
    matrix.append([int(num) for num in input().split()])

x, y = 0, 0
for r in range(N):
    for c in range(N):
        if matrix[r][c] == 9:
            x = r
            y = c
            matrix[r][c] = 0
            break

answer = 0
count = 0
weight = 2
while True:
    queue = deque([])
    queue.append([x, y, 0])
    visited = [[False]*N for _ in range(N)]
    t_max = int(10e9)
    x_target = 100
    y_target = 100
    flag = False
    while queue:
        x_orig, y_orig, t = queue.popleft()
        if t > t_max:
            break
        visited[x_orig][y_orig] = True
        for i in range(4):
            nx = x_orig + dx[i]
            ny = y_orig + dy[i]
            if 0<=nx<N and 0<=ny<N and visited[nx][ny] == False:
                if matrix[nx][ny] == 0 or matrix[nx][ny] == weight:
                    queue.append([nx, ny, t+1])
                    visited[nx][ny] = True
                elif matrix[nx][ny] < weight:
                    t_max = t
                    if nx < x_target:
                        x_target = nx
                        y_target = ny
                    elif nx == x_target:
                        if ny < y_target:
                            x_target = nx
                            y_target = ny
                    flag = True
    if flag:
        count += 1
        answer += (t_max+1)
        x = x_target
        y = y_target
        matrix[x][y] = 0

        if count == weight:
            weight += 1
            count = 0
    else:
        break
print(answer)