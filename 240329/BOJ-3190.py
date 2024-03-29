import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
# 0은 아무것도 없음
# 1은 뱀
# 2는 사과
matrix = [[0]*(N+1) for _ in range(N+1)]
matrix[1][1] = 1
K = int(input())
for _ in range(K):
    x, y = map(int, input().split())
    matrix[x][y] = 2

L = int(input())
change = []
for _ in range(L):
    x, c = map(str, input().rstrip().split())
    x = int(x)
    change.append([x, c])

# 0은 동, 1은 남, 2는 서, 3은 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 초기 방향
dir = 0
# 확인할 change index
index = 0

# 처음 뱀의 위치 설정, queue에 넣어줌
x, y = 1, 1
q = deque([])
q.append([1, 1])
answer = 0
while True:
    answer += 1

    nx = x + dx[dir]
    ny = y + dy[dir]
    if 0 < nx <= N and 0 < ny <=N:
        if matrix[nx][ny] == 0:
            q.append([nx, ny])
            matrix[nx][ny] = 1
            d = q.popleft()
            matrix[d[0]][d[1]] = 0
        elif matrix[nx][ny] == 1:
            break
        elif matrix[nx][ny] == 2:
            q.append([nx, ny])
            matrix[nx][ny] = 1
    else:
        break
    x = nx
    y = ny

    if index < len(change) and answer == change[index][0]:
        if change[index][1] == 'L':
            dir = (dir-1) % 4
        elif change[index][1] == 'D':
            dir = (dir+1) % 4
        index += 1
print(answer)