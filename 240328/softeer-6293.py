import sys
input = sys.stdin.readline

N = int(input())
rock = [int(num) for num in input().split()]

dp = [1] * N
for i in range(1, N):
    find = 0
    for j in range(i):
        if rock[i] > rock[j]:
            find = max(find, dp[j])
    dp[i] = find + 1

print(max(dp))