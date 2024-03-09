R, C = map(int, input().split())
matrix = [[True] * C for _ in range(R)]

k = int(input())
for _ in range(k):
    br, bc = map(int, input().split())
    matrix[br][bc] = False

sr, sc = map(int, input().split())
x = sr
y = sc
matrix[x][y] = False

# 방향에 대한 정보 저장 받아서 dx, dy로 저장
direction = [int(num) for num in input().split()]
dx = []
dy = []
for i in range(4):
    if direction[i] == 1:
        dx.append(-1)
        dy.append(0)
    elif direction[i] == 2:
        dx.append(1)
        dy.append(0)
    elif direction[i] == 3:
        dx.append(0)
        dy.append(-1)
    else:
        dx.append(0)
        dy.append(1)


# 로봇 움직일 수 있는 경우인지를 표현하는 flag
flag = True
# 초기 방향
# mod 연산으로 0, 1, 2, 3만 저장
dir = 0
while flag:
    # 로봇 움직일 수 없다고 가정하고 false로 저장해둠
    flag = False
    # 4가지 방향이 최대이니 4번 반복문 돌림
    for _ in range(4):
        nx = x + dx[dir]
        ny = y + dy[dir]

        # 해당 방향으로 이동이 가능한 경우
        # dir은 지정한 방향 일직선으로 움직이니 방향은 수정 X
        if 0 <= nx < R and 0 <= ny < C and matrix[nx][ny] == True:
            x = nx
            y = NotADirectoryError
            matrix[x][y] = False
            flag = True
            break

        # mod 4 연산으로 방향 1씩 증가
        dir = (dir + 1) % 4

# 로봇 움직일 수 없을 때의 위치 출력
print(x, y)