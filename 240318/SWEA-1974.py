T = int(input())

for test_case in range(1, T+1):
    # matrix 입력 받아 생성
    matrix = []
    for i in range(9):
        matrix.append([int(num) for num in input().split()])
    answer = 1
    
    # row 기준으로 스도쿠 만족하는지 확인
    for i in range(9):
        s = set(matrix[i])
        if len(s) != 9:
            answer = 0
    if answer == 0:
        print('#{0} {1}'.format(test_case, answer))
        continue

    # col 기준으로 스도쿠 만족하는지 확인
    for i in range(9):
        s = set()
        for j in range(9):
            s.add(matrix[j][i])
        if len(s) != 9:
            answer = 0
    if answer == 0:
        print('#{0} {1}'.format(test_case, answer))
        continue

    # 3*3 기준으로 스도쿠 만족하는지 확인
    dx = [0, 0, 0, 1, 1, 1, 2, 2, 2]
    dy = [0, 1, 2, 0, 1, 2, 0, 1, 2]
    for x in range(0,9,3):
        for y in range(0, 9, 3):
            s = set()
            for i in range(9):
                nx = x + dx[i]
                ny = y + dy[i]
                s.add(matrix[nx][ny])
            if len(s) != 9:
                answer = 0

    print('#{0} {1}'.format(test_case, answer))