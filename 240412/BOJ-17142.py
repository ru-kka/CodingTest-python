import copy
from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int, input().split())
matrix = []
for _ in range(N):
    matrix.append([int(num) for num in input().split()])

virus = []
for r in range(N):
    for c in range(N):
        if matrix[r][c] == 2:
            virus.append([r, c])

def choose_virus(count, index, graph):
    if count == M:
        bfs(graph)
        return
    if index >= len(virus):
        return
    
    graph_copy = copy.deepcopy(graph)
    # 바이러스 선택하지 않았을 때
    choose_virus(count, index+1, graph_copy)
    # 바이러스 선택했을 때
    graph_copy[virus[index][0]][virus[index][1]] = 3
    choose_virus(count+1, index+1, graph_copy)

def bfs(graph):
    global min_time
    queue = deque([])
    blank_num = 0
    for r in range(N):
        for c in range(N):
            if graph[r][c] == 3:
                queue.append([r, c, 0])
            elif graph[r][c] == 0:
                blank_num += 1
    if blank_num == 0:
        min_time = 0
        return

    cnt = 0
    while queue:
        x, y, t = queue.popleft()
        if t >= min_time:
            return
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N:
                if graph[nx][ny] == 0:
                    cnt += 1
                    if cnt == blank_num:
                        min_time = min(min_time, t+1)
                    graph[nx][ny] = 4
                    queue.append([nx, ny, t+1])
                elif graph[nx][ny] == 2:
                    graph[nx][ny] = 3
                    queue.append([nx, ny, t+1])

min_time = int(10e9)
choose_virus(0, 0, matrix)

if min_time == int(10e9):
    print(-1)
else:
    print(min_time)