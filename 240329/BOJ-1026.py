import sys
input = sys.stdin.readline

N = int(input())
A = [int(num) for num in input().split()]
B = [int(num) for num in input().split()]

A = sorted(A, key=lambda x:x)
B = sorted(B, key=lambda x:x, reverse=True)

answer = 0
for i in range(N):
    answer += A[i] * B[i]

print(answer)