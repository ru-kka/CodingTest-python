N = int(input())

answer = -1
standard = N // 5
for i in range(standard,-1,-1):
    cnt = i
    left = N - 5 * i
    if left % 3 == 0:
        cnt += left // 3
        answer = cnt
        break

print(answer)