import sys
input = sys.stdin.readline

N, M, x, y, K = map(int, input().split())
matrix = []
for _ in range(N):
    matrix.append([int(num) for num in input().split()])
dice = [0, 0, 0, 0, 0, 0]

op = [int(num) for num in input().split()]                                
for o in op:
    if o == 1:
        if 0<=y+1<M:
            y += 1
            tmp = dice[5]
            dice[5] = dice[1]
            dice[1] = dice[0]
            dice[0] = dice[2]
            dice[2] = tmp

            if matrix[x][y] == 0:
                matrix[x][y] = dice[5]
            else:
                dice[5] = matrix[x][y]
                matrix[x][y] = 0
            print(dice[0])

    elif o == 2:
        if 0<=y-1<M:
            y -= 1
            tmp = dice[5]
            dice[5] = dice[2]
            dice[2] = dice[0]
            dice[0] = dice[1]
            dice[1] = tmp

            if matrix[x][y] == 0:
                matrix[x][y] = dice[5]
            else:
                dice[5] = matrix[x][y]
                matrix[x][y] = 0
            print(dice[0])

    elif o == 3:
        if 0<=x-1<N:
            x -= 1
            tmp = dice[5]
            dice[5] = dice[3]
            dice[3] = dice[0]
            dice[0] = dice[4]
            dice[4] = tmp

            if matrix[x][y] == 0:
                matrix[x][y] = dice[5]
            else:
                dice[5] = matrix[x][y]
                matrix[x][y] = 0
            print(dice[0])

    elif o == 4:
        if 0<=x+1<N:
            x += 1
            tmp = dice[5]
            dice[5] = dice[4]
            dice[4] = dice[0]
            dice[0] = dice[3]
            dice[3] = tmp

            if matrix[x][y] == 0:
                matrix[x][y] = dice[5]
            else:
                dice[5] = matrix[x][y]
                matrix[x][y] = 0
            print(dice[0])