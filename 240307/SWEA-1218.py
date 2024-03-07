from collections import deque

T = 10
# 괄호 여는 것 닫는 것 각각 저장해둠
left = ['(', '[', '{', '<']
right = [')', ']', '}', '>']
for test_case in range(1, T+1):
    N = int(input())
    string = input()
    q = deque()
    answer = 1
    # 문자열 전체 탐색
    for s in string:
        # 괄호 여는 것 들어오면 queue에 넣음
        if s in left:
            q.append(s)
        # 괄호 닫는 것 들어올 때
        else:
            # queue가 비어있으면 유효X
            if len(q) == 0:
                answer = 0
                break
            else:
                pop = q.pop()
                # 괄호 여는 것과 쌍을 이루면 유효O
                if right.index(s) == left.index(pop):
                    continue
                # 괄호 여는 것과 쌍을 이루지 않으면 유효X
                else:
                    answer = 0
                    break
    
    print('#{0} {1}'.format(test_case, answer))