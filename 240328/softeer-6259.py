import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
n = [int(num) for num in input().split()]
m = [int(num) for num in input().split()]

dp = [[0] * (M) for _ in range(N)]
answer = 0
for i in range(N):
    for j in range(M):
        if n[i] == m[j]:
            if 0<= i-1 <N and 0<= j-1 <M and dp[i-1][j-1] != 0:
                dp[i][j] = dp[i-1][j-1] + 1
                answer = max(answer, dp[i][j] )
            else:
                dp[i][j] = 1
                answer = max(answer, 1)

print(answer)