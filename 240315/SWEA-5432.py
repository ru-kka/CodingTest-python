T = int(input())
for test_case in range(1, T+1):
    expression = input()
    stack = []
    # 직전에 들어온 괄호에 따라 flag 표현
    # (는 True, )는 False
    flag = False
    answer = 0
    for e in expression:
        # ( 들어오면 True로 바꾸고 스택에 넣음
        if e == '(':
            flag = True
            stack.append('(')
        # ) 들어았을 때
        elif e == ')':
            # 스택에서 ( 1개 빼고
            stack.pop()
            # flag가 True이면 레이저 위치
            if flag == True:
                # answer 스택 길이만큼 더해줌
                answer += len(stack)
            # flag가 Flase이면 쇠막대기 끝부분
            else:
                # answer 1 더해줌
                # 2번 자르면 3개이고 3번 자르면 4개가 되는 것 적용
                answer += 1
            # flag False로 바꿈
            flag = False
    
    # 출력
    print('#{0} {1}'.format(test_case, answer))