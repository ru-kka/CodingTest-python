from itertools import combinations

N, M = map(int, input().split())
card = [int(num) for num in input().split()]
# 조합 사용하여 모든 경우 배열로 생성
combi_card = list(combinations(card, 3))

# M이하면서 M과 가장 가까운 sum 값 찾음
answer = 0
for l in combi_card:
    if M >= sum(l) and sum(l) > answer:
        answer = sum(l)

print(answer)