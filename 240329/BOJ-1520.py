import sys
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = []
for _ in range(N):
    l = [int(num) for num in input().split()]
    matrix.append(l)

dp = [[-1]*M for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):
    if x == N-1 and y == M-1:
        return 1
    if dp[x][y] != -1:
        return dp[x][y]
    
    cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<N and 0<=ny<M and matrix[x][y] > matrix[nx][ny]:
            cnt += dfs(nx,ny)
    dp[x][y] = cnt
    return dp[x][y]

answer = dfs(0, 0)
print(answer)