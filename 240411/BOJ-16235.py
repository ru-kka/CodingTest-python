from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

N, M, K = map(int, input().split())
matrix = [[5]*N for _ in range(N)]
A = []
for r in range(N):
    A.append([int(num) for num in input().split()])

tree = [[deque() for _ in range(N)] for _ in range(N)]
for _ in range(M):
    x, y, z = map(int, input().split())
    tree[x-1][y-1].append(z)

def spring_and_summer():
    global matrix
    global tree
    for r in range(N):
        for c in range(N):
            length = len(tree[r][c])
            for i in range(length):
                if matrix[r][c] >= tree[r][c][i]:
                    matrix[r][c] -= tree[r][c][i]
                    tree[r][c][i] += 1
                else:
                    for _ in range(i, length):
                        matrix[r][c] += tree[r][c].pop()//2
                    break

def fall_and_winter():
    global tree
    for r in range(N):
        for c in range(N):
            for age in tree[r][c]:
                if age % 5 == 0:
                    for i in range(8):
                        nx = r + dx[i]
                        ny = c + dy[i]
                        if 0<=nx<N and 0<=ny<N:
                            tree[nx][ny].appendleft(1)
            matrix[r][c] += A[r][c]

for _ in range(K):
    spring_and_summer()
    fall_and_winter()

answer = 0
for r in range(N):
    for c in range(N):
        answer += len(tree[r][c])
print(answer)