import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = []
for _ in range(N):
    r = [int(num) for num in input().split()]
    matrix.append(r)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(visited):
    q = deque([])
    q.append([0,0])
    visited[0][0] += 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M:
                if matrix[nx][ny] == 0:
                    if visited[nx][ny] == 0:
                        visited[nx][ny] += 1
                        q.append([nx, ny])
                else:
                    visited[nx][ny] += 1
                    
def check(visited):
    status = False
    cnt = 0
    for x in range(1, N):
        for y in range(1, M):
            if matrix[x][y] == 1:
                if visited[x][y] >= 2:
                    matrix[x][y] = 0
                    cnt += 1
                else:
                    status = True
    return cnt, status

status = True
answer = 0
while status:
    visited = [[0] * (M) for _ in range(N)]
    bfs(visited)
    cnt, status = check(visited)
    if cnt != 0:
        answer += 1

print(answer)