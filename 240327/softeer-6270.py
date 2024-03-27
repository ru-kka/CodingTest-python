N, M = map(int, input().split())
standard = [0]
for _ in range(N):
    length, speed = map(int, input().split())
    for _ in range(length):
        standard.append(speed)

answer = 0
length_start = 1
for _ in range(M):
    length, speed = map(int, input().split())
    for l in range(length_start, length_start+length):
        answer = max(answer, speed - standard[l])
    length_start += length

print(answer)