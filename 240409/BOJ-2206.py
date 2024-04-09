import sys
input = sys.stdin.readline

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int, input().split())
matrix = [[0] for _ in range(N+1)]
for r in range(1, N+1):
    string = input().rstrip()
    for s in string:
        matrix[r].append(int(s))

visited_0 = [[-1]*(M+1) for _ in range(N+1)]
visited_0[1][1] = 1

visited_1 = [[-1]*(M+1) for _ in range(N+1)]
visited_1[1][1] = 1

q = deque()
q.append([1, 1, 0])
while q:
    flag = False
    p = q.popleft()
    if p[0] == N and p[1] == M:
        break
    for i in range(4):
        nx = p[0] + dx[i]
        ny = p[1] + dy[i]
        if 1<=nx<(N+1) and 1<=ny<(M+1):
            if p[2] == 0 and visited_0[nx][ny] == -1:
                if matrix[nx][ny] == 0:
                    q.append([nx, ny, 0])
                    visited_0[nx][ny] = visited_0[p[0]][p[1]] + 1
                elif matrix[nx][ny] == 1:
                    q.append([nx, ny, 1])
                    visited_1[nx][ny] = visited_0[p[0]][p[1]] + 1
            elif p[2] == 1 and matrix[nx][ny] == 0 and visited_1[nx][ny] == -1:
                q.append([nx, ny, 1])
                visited_1[nx][ny] = visited_1[p[0]][p[1]] + 1

if visited_0[N][M] != -1 and visited_1[N][M] != -1:
    print(min(visited_0[N][M], visited_1[N][M]))
else:
    print(max(visited_0[N][M], visited_1[N][M]))