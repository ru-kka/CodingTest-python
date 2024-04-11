import sys
input = sys.stdin.readline

N = int(input())
number = [int(num) for num in input().split()]

B, C = map(int, input().split())

answer = 0
for n in number:
    answer += 1
    n -= B
    if n > 0:
        answer += n // C
        if n % C != 0:
            answer += 1
print(answer)