import sys
inpuy = sys.stdin.readline

import copy

dx = [-1, 0, 1 ,0]
dy = [0, 1 , 0, -1]

cctv_direction = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [0, 3]],
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
    [[0, 1, 2, 3]]
]

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append([int(num) for num in input().split()])

cctv = []
for r in range(N):
    for c in range(M):
        if graph[r][c] != 0 and graph[r][c] != 6:
            cctv.append([graph[r][c], r, c])

def fill(direction, x, y, matrix_copy):
    for d in direction:
        nx = x
        ny = y
        while True:
            nx += dx[d]
            ny += dy[d]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                break
            if matrix_copy[nx][ny] == 6:
                break
            elif matrix_copy[nx][ny] == 0:
                matrix_copy[nx][ny] = 7

def dfs(cnt , matrix):
    global answer
    if cnt == len(cctv):
        count = 0
        for r in range(N):
            for c in range(M):
                if matrix[r][c] == 0:
                    count += 1
        answer = min(answer, count)
        return
    
    matrix_copy = copy.deepcopy(matrix)
    for direction in cctv_direction[cctv[cnt][0]]:
        x = cctv[cnt][1]
        y = cctv[cnt][2]
        fill(direction, x, y, matrix_copy)
        dfs(cnt+1, matrix_copy)
        matrix_copy = copy.deepcopy(matrix)

answer = int(10e9)
dfs(0, graph)
print(answer)