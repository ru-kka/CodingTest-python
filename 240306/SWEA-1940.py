T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    speed = 0
    distance = 0
    for _ in range(N):
        s = input()
        # 입력이 0인지 아닌지 먼저 판단
        if s[0] != '0':
            n, c = map(int, s.split())

            # 입력 1과 2에 따라 각각 다음과 같이
            if n == 1:
                speed += c
            elif n == 2:
                if speed >= c:
                    speed -= c
                else:
                    speed = 0
            
        distance += speed
    
    print('#{0} {1}'.format(test_case, distance))