T = int(input())
for test_case in range(1, T + 1):
    # 입력 문자열 세로로 저장하기 위해 15행 임의의로 생성
    e = [[] for _ in range(15)]
    # 입력 문자열 중 최대 길이 저장할 변수 생성
    length = 0
    for index in range(5):
        string = input()
        # 입력 문자열 세로로 저장
        for i, s in enumerate(string):
            e[i].append(s)
        if len(string) > length:
            length = len(string)
            
    # 입력 문자열 중 가장 긴 문자열 길이까지 e matrix의 행 탐색
    result = ''
    for index in range(length):
        result += ''.join(e[index])
     
    print('#{0} {1}'.format(test_case, result))