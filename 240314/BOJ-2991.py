A, B, C, D = map(int, input().split())
time = [int(num) for num in input().split()]

answer = [0] * 3
for index, t in enumerate(time):
    # 첫번째 개 반복시간으로 나눠서 나머지 구함
    r1 = t % (A+B)
    # 해당 나머지가 짖는 범위이면 1증가
    if 0 < r1 <= A:
        answer[index] += 1

    # 두번째 개 반복시간으로 나눠서 나머지 구함
    r2 = t % (C+D)
    # 해당 나머지가 짖는 범위이면 1증가
    if 0 < r2 <= C:
        answer[index] += 1

for a in answer:
    print(a)