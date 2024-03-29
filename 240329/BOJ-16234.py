import sys
from collections import deque
input = sys.stdin.readline

N, L, R = map(int, input().split())
matrix = []
for i in range(N):
    l = [int(num) for num in input().split()]
    matrix.append(l)

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, visited):
    q = deque([])
    q.append([x, y])
    union = []
    union.append([x, y])

    while q:
        p = q.popleft()
        for i in range(4):
            nx = p[0] + dx[i]
            ny = p[1] + dy[i]

            if 0<=nx<N and 0<=ny<N and visited[nx][ny] == False and L<=abs(matrix[p[0]][p[1]] - matrix[nx][ny])<=R:
                visited[nx][ny] = True
                union.append([nx, ny])
                q.append([nx, ny])
    
    if len(union) <= 1:
        return False
    else:
        total_sum = 0
        for state in union:
            total_sum += matrix[state[0]][state[1]]
        for state in union:
            matrix[state[0]][state[1]] = total_sum // len(union)
        return True

flag = True
answer = 0
while flag:
    flag = False
    
    visited = [[False]*N for _ in range(N)]
    for x in range(N):
        for y in range(N):
            if visited[x][y] == False:
                visited[x][y] = True
                if bfs(x, y, visited):
                    flag = True

    if flag == True:
        answer += 1

print(answer)