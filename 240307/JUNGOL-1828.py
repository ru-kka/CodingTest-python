N = int(input())
chemi = []
for _ in range(N):
    x, y = map(int, input().split())
    chemi.append([x, y])
# 화학 물질 최저, 최고 간견 좁은 순으로 sorting
chemi = sorted(chemi, key=lambda x : x[1] - x[0])

ref = [chemi[0]]
for i in range(1, N):
    # 화학 물질의 최저, 최고 온도
    min_c = chemi[i][0]
    max_c = chemi[i][1]
    flag = False
    # 현재 냉장고 전체 탐색
    for r in ref:
        # 냉장고 최저, 최고 온도
        r_min = r[0]
        r_max = r[1]
        # 화학 물질이 냉장고 범위에 포함될 경우
        if r_min <= max_c and r_max >= min_c:
            # 화학 물질 최저 온도가 냉장고 최저 온도보다 높을 경우
            if r_min < min_c:
                r[0] = min_c
            # 화학 물질 최고 온도가 냉장고 최고 온도보다 낮을 경우
            if r_max > max_c:
                r[1] = max_c
            flag = True
            break
    # 화학 물질이 들어갈 냉장고 찾지 못했을 경우
    # 냉장고 1개 더 추가
    if flag == False:
        ref.append(chemi[i])
        
# 냉장고 길이 출력으로 냉장고의 대수 출력
print(len(ref))