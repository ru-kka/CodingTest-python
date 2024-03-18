T = int(input())

for test_case in range(1, T+1):
    N, M, K = map(int, input().split())
    time = [int(num) for num in input().split()]
    # 오름차순으로 정렬
    time.sort()

    # 붕어빵 개수
    num = 0
    # 붕어빵 증가를 계산할 시점
    # (M으로 나누어 몫 - 시점)*K만큼 붕어빵 개수 더해주면 됨
    start = 0
    answer = 'Possible'
    # time 전체 탐색
    for t in time:
        # (M으로 나누어 몫 - 시점)*K만큼 붕어빵 개수 더해주면 됨
        num += ((t // M) - start) * K
        # 붕어빵 개수 한개 줄임
        num -= 1
        if num < 0:
            answer = 'Impossible'
            break
        # 시점을 M으로 나눈 몫으로 설정
        start = t // M
    
    print('#{0} {1}'.format(test_case, answer))