T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    matrix = []
    for _ in range(N):
        matrix.append([int(num) for num in input().split()])
    
    answer = 0
    # 왼쪽 모서리 시작 시점 기준 탐색
    for x in range(N-M+1):
        for y in range(N-M+1):
            sum = 0
            # 왼쪽 모서리 시작 기준 M*M 더했을 때의 값 구하기
            for i in range(M):
                for j in range(M):
                    sum += matrix[x+i][y+j]
            # 최대 비교
            answer = max(answer, sum)

    print('#{0} {1}'.format(test_case, answer))