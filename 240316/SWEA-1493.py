# 대각선 시작 기준으로 index, standard 정함
def find_index(num):
    cnt = 1
    n = 1
    while num >= n:
        n += cnt
        cnt += 1
    return cnt - 1, n - (cnt - 1)

# 대각선끼리는 x,y 더한 값 일정한 것 이용
def find_xy(num, index, standard):
    # 기준 값과 차이 만큼으로 x,y 좌표 구함
    x = 1 + (num - standard)
    y = index - (num - standard)
    return x, y

T = int(input())
for test_case in range(1, T+1):
    p, q = map(int, input().split())

    # p, q 각각 기준되는 대각선 찾음
    p_index, p_standard = find_index(p)
    q_index, q_standard = find_index(q)

    # p, q의 x,y 좌표 구함
    p_x, p_y = find_xy(p, p_index, p_standard)
    q_x, q_y = find_xy(q, q_index, q_standard)

    x = p_x + q_x
    y = p_y + q_y

    # 대각선 시작하는 값 기준으로 반복문 돌려서 기준 값 찾음
    answer = 1
    cnt = 1
    for _ in range(1, x+y-1):
        answer += cnt
        cnt += 1
    # 그 기준값부터 x-1 값 더함
    # x 2이면 대각선 기준에서 1증가..
    answer += x-1

    print('#{0} {1}'.format(test_case, answer))