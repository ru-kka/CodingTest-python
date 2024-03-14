N = int(input())
stack = []

answer = [0] * (N+1)
for i in range(1, N+1):
    h = int(input())
    # 스택에 요소가 있는 경우
    while stack:
        # 스택 마지막 요소의 길이가 새로운 빌딩 높이보다 낮으면
        if stack[-1][1] < h:
            # 마지막 요소 빌딩의 보이는 것은 새로운 빌딩 번째수
            answer[stack[-1][0]] = i
            # 마지막 요소 빌딩은 stack에서 pop
            stack.pop()
        else:
            # 마지막 요소 길이가 새로운 빌딩 높이 이상이면 비교하지 않음
            break
    
    # stack에는 새로운 빌딩 번째수, 높이 append
    stack.append([i, h])

# 정답 출력
for a in answer[1:]:
    print(a)