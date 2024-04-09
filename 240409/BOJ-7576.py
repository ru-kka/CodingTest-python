import sys
input  = sys.stdin.readline

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, matrix):
    next_in = []
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<N and 0<=ny<M and matrix[nx][ny] == 0:
            matrix[nx][ny] = 1
            next_in.append([nx, ny])
    return next_in

M, N = map(int, input().split())
matrix = []
for _ in range(N):
    row = [int(num) for num in input().split()]
    matrix.append(row)

q = deque()
for r in range(N):
    for c in range(M):
        if matrix[r][c] == 1:
            q.append([r, c])

flag = False
answer = 0
while True:
    nq = deque()
    while q:
        x, y = q.popleft()
        next_in = bfs(x, y, matrix)
        for x, y in next_in:
            nq.append([x, y])
    q = nq

    if len(q) == 0:
        for r in range(N):
            for c in range(M):
                if matrix[r][c] == 0:
                    flag = True
                    break
            if flag:
                break
        break

    answer += 1

if flag:
    print(-1)
else:
    print(answer)