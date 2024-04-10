import sys
input = sys.stdin.readline

from itertools import combinations
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int, input().split())
matrix = []
for _ in range(N):
    l = [int(num) for num in input().split()]
    matrix.append(l)

zero_position = []
for r in range(N):
    for c in range(M):
        if matrix[r][c] == 0:
            zero_position.append([r, c])

zero_position_com = list(combinations(zero_position, 3))

answer = 0
for com in zero_position_com:
    queue = deque([])
    matrix_case = [[0] * M for _ in range(N)]
    for r in range(N):
        for c in range(M):
            matrix_case[r][c] = matrix[r][c]
            if matrix[r][c] == 2:
                queue.append([r,c])
    for c in com:
        matrix_case[c[0]][c[1]] = 1
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M and matrix_case[nx][ny] == 0:
                matrix_case[nx][ny] = 2
                queue.append([nx, ny])
    cnt = 0
    for r in range(N):
        for c in range(M):
            if matrix_case[r][c] == 0:
                cnt += 1
    answer = max(answer, cnt)

print(answer)