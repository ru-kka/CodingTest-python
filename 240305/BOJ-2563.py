N = int(input())

# 100 * 100 0 matrix 생성
matrix = [[0] * 100 for _ in range(100)]
# 왼쪽 모서리 기준 색 칠해지는 부분 1로 변경
for _ in range(N):
    x, y = map(int, input().split())

    for nx in range(x, x + 10):
        for ny in range(y, y + 10):
            matrix[nx][ny] = 1

# 색 칠해져 있는 부분 탐색
answer = 0
for x in range(0, 100):
    for y in range(0, 100):
        if matrix[x][y] == 1:
            answer += 1

print(answer)