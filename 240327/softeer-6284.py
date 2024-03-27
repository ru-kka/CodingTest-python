number = 1000000007

K, P, N = map(int, input().split())

num = K
for _ in range(N):
    num *= P
    if num >= number:
        num = num % number

print(num)