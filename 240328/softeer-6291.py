import sys
from heapq import heapify, heappush, heappop

N = int(sys.stdin.readline())
time = []
for _ in range(N):
    s, f = map(int, sys.stdin.readline().split())
    heappush(time, (f, s))

answer = 0
end = 0
while time:
    f, s = heappop(time)
    if s >= end:
        answer += 1
        end = f

print(answer)