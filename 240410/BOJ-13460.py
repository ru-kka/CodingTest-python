from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0 ,0, -1, 1]

N, M = map(int, input().split())
rx, ry, bx, by = 0, 0, 0, 0
visited = []
queue = deque()

matrix = []
for r in range(N):
    string = input()
    l = []
    for c, s in enumerate(string):
        if s == 'R':
            rx = r
            ry = c
        elif s == 'B':
            bx = r
            by = c
        l.append(s)
    matrix.append(l)
visited.append([rx, ry, bx, by])
queue.append([rx, ry, bx, by, 1])

def move(x, y, i, j):
    count = 0
    while matrix[x+i][y+j] != '#' and matrix[x][y] != 'O':
        x += i
        y += j
        count += 1
    return x, y, count

def bfs():
    while queue:
        rx, ry, bx, by, cnt = queue.popleft()
        if cnt > 10:
            break
        for i in range(4):
            nrx, nry, rCnt = move(rx, ry, dx[i], dy[i])
            nbx, nby, bCnt = move(bx, by, dx[i], dy[i])

            if matrix[nbx][nby] == 'O':
                continue
            if matrix[nrx][nry] == 'O':
                return cnt
            
            if nrx == nbx and nry == nby:
                if rCnt > bCnt:
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]
            
            if [nrx, nry, nbx, nby] not in visited:
                visited.append([nrx, nry, nbx, nby])
                queue.append([nrx, nry, nbx, nby, cnt+1])
    return -1
print(bfs())