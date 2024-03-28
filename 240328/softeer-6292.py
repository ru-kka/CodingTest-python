import sys
input = sys.stdin.readline

number = 1000000007

def recur(p, n):
    if n == 1:
        return p

    elif n % 2 == 0:
        a = recur(p, n // 2)
        return a * a % number

    else:
        b = recur(p, (n - 1) // 2)
        return b * b * p % number


K, P, N = list(map(int, input().split()))
result = recur(P, 10*N)
result *= K
print(result % number)