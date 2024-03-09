N = int(input())
inform = []
for _ in range(N):
    w, h = map(int, input().split())
    inform.append([w, h])

# rank 저장
rank = [0] * N
# 전체 비교
for i in range(N):
    for j in range(i+1, N):
        # i가 덩치 더 큰 경우
        if inform[i][0] > inform[j][0] and inform[i][1] > inform[j][1]:
            rank[j] += 1
        # j가 덩치 더 큰 경우
        if inform[i][0] < inform[j][0] and inform[i][1] < inform[j][1]:
            rank[i] += 1


# rank 출력
for r in rank:
    print(r+1, end=" ")