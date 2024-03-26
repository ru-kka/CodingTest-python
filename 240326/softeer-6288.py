W, N = map(int, input().split())
type = []
for _ in range(N):
    m, p = map(int, input().split())
    type.append([m, p])

type = sorted(type, key=lambda x:x[1], reverse=True)

weight = 0
answer = 0
for t in type:
    if weight + t[0] <= W:
        weight += t[0]
        answer += t[0] * t[1]
    else:
        answer += (W-weight) * t[1]
        break

print(answer)