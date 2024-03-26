N, d, k, c = map(int, input().split())
sushi = []
for _ in range(N):
    sushi.append(int(input()))

answer = 0
for i in range(N):
    if i + (k-1) > N-1:
        s = sushi[i:] + sushi[:k-(N-i)]
    else:
        s = sushi[i:i+k]
    
    s.append(c)
    s_set = set(s)
    answer = max(len(s_set), answer)

print(answer)