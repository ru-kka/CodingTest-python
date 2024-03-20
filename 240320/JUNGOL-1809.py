N = int(input())
top = [int(num) for num in input().split()]

stack = []
answer = [0] * (N+1)
for i in range(len(top)):
    # 오른쪽 탑부터 생각
    t = top[(N-1)-i]
    index = N-i

    while stack:
        # 스택에 들어가 있는 마지막 탑 높이가 지금 들어갈 탑 높이보다 낮으면
        if stack[-1][0] < t:
            # 스택 마지막 탑 이 지금 들어갈 탑으로 레이저 발사한다고 생각 
            answer[stack[-1][1]] = index
            # 스택에서 꺼냄
            stack.pop()
        # 그렇지 않을 경우 반복문 종료
        else:
            break
    # 스택에 지금 들어갈 탑은 무조건 넣음
    stack.append([t, index])

# 출력
for i in range(1, N+1):
    print(answer[i], end=" ")