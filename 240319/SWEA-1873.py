T = int(input())

for test_case in  range(1, T+1):
    H, W = map(int, input().split())
    matrix = []
    # 전차 위치
    tank_x = 0
    tank_y = 0
    # 전차 방향
    # 상, 하, 좌, 우
    tank_status = 0
    for i in range(H):
        str = input()
        l = []
        for j, s in enumerate(str):
            if s == '^' or s == 'v' or s == '<' or s == '>':
                tank_x = i
                tank_y = j
                tank_status = ['^', 'v', '<', '>'].index(s)
            l.append(s)
        matrix.append(l)
    
    N = int(input())
    op = input()
    for o in op:
        # 상하좌우 명령의 경우 방향 바꾸고 움직일 수 있는 경우 움직임
        if o == 'U':
            matrix[tank_x][tank_y] = '^'
            tank_status = 0
            if 0<= tank_x - 1 < H and matrix[tank_x - 1][tank_y] == '.':
                matrix[tank_x][tank_y] = '.'
                tank_x -= 1
                matrix[tank_x][tank_y] = '^'
        if o == 'D':
            matrix[tank_x][tank_y] = 'v'
            tank_status = 1
            if 0<= tank_x + 1 < H and matrix[tank_x + 1][tank_y] == '.':
                matrix[tank_x][tank_y] = '.'
                tank_x += 1
                matrix[tank_x][tank_y] = 'v'
        if o == 'L':
            matrix[tank_x][tank_y] = '<'
            tank_status = 2
            if 0<= tank_y - 1 < W and matrix[tank_x][tank_y - 1] == '.':
                matrix[tank_x][tank_y] = '.'
                tank_y -= 1
                matrix[tank_x][tank_y] = '<'
        if o == 'R':
            matrix[tank_x][tank_y] = '>'
            tank_status = 3
            if 0<= tank_y + 1 < W and matrix[tank_x][tank_y + 1] == '.':
                matrix[tank_x][tank_y] = '.'
                tank_y += 1
                matrix[tank_x][tank_y] = '>'
        # 포탄 발사 경우
        # 포탄 발사 방향으로 matrix 끝까지 가며 벽, 강철 확인함
        # 벽, 강철 만났을 경우 요구사항에 맞게 동작하게함
        if o == 'S':
            if tank_status == 0:
                d = tank_x
                while d - 1 >= 0:
                    if matrix[d - 1][tank_y] == '*':
                        matrix[d - 1][tank_y] = '.'
                        break
                    elif matrix[d - 1][tank_y] == '#':
                        break
                    d -= 1
            elif tank_status == 1:
                d = tank_x
                while d + 1 < H:
                    if matrix[d + 1][tank_y] == '*':
                        matrix[d + 1][tank_y] = '.'
                        break
                    elif matrix[d + 1][tank_y] == '#':
                        break
                    d += 1
            elif tank_status == 2:
                d = tank_y
                while d - 1 >= 0:
                    if matrix[tank_x][d - 1] == '*':
                        matrix[tank_x][d - 1] = '.'
                        break
                    elif matrix[tank_x][d - 1] == '#':
                        break
                    d -= 1
            else: # tank_status == 3
                d = tank_y
                while d + 1 < W:
                    if matrix[tank_x][d + 1] == '*':
                        matrix[tank_x][d + 1] = '.'
                        break
                    elif matrix[tank_x][d + 1] == '#':
                        break
                    d += 1
    
    # 출력
    print('#{0} '.format(test_case), end="")
    for i in range(H):
        print(''.join(matrix[i]))