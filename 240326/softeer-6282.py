from collections import deque

N = int(input())
matrix = [[int(num) for num in input().rstrip()] for _ in range(N)]
# matrix = [list(input().rstrip()) for _ in range(N)]
# matrix = []
# for i in range(N):
#     row = input()
#     l = []
#     for r in row:
#         l.append(int(r))
#     matrix.append(l)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    q = deque([[x, y]])
    cnt = 1
    while q:
        p = q.popleft()
        for i in range(4):
            nx = p[0] + dx[i]
            ny = p[1] + dy[i]
            if 0<= nx < N and 0 <= ny < N and matrix[nx][ny] == 1:
                matrix[nx][ny] = 0
                cnt += 1
                q.append([nx, ny])
    
    return cnt

answer = []
for x in range(N):
    for y in range(N):
        if matrix[x][y] == 1:
            matrix[x][y] = 0
            answer.append(dfs(x, y))

answer.sort()
print(len(answer))
for a in answer:
    print(a)