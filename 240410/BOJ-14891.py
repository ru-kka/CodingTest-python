import sys
input = sys.stdin.readline

from collections import deque

wheel = [0]
wheel.append(list(map(int, input().rstrip())))
wheel.append(list(map(int, input().rstrip())))
wheel.append(list(map(int, input().rstrip())))
wheel.append(list(map(int, input().rstrip())))

def left_change(n, direction):
    if wheel[n][6] != wheel[n-1][2]:
        return (-1)*direction
    return 0

def right_change(n, direction):
    if wheel[n][2] != wheel[n+1][6]:
        return (-1)*direction
    return 0

answer = 0
K = int(input())
for _ in range(K):
    num, direction = map(int, input().split())
    direction_list = deque([direction])

    left_direction = direction
    for n in range(num, 1, -1):
        left_direction = left_change(n, left_direction)
        direction_list.appendleft(left_direction)

    right_direction = direction
    for n in range(num, 4):
        right_direction = right_change(n, right_direction)
        direction_list.append(right_direction)
    
    for index, d in enumerate(direction_list):
        if d == 1:
            w_q = deque(wheel[index+1])
            w_q.appendleft(w_q.pop())
            w_q = list(w_q)
            wheel[index+1] = w_q
        elif d == -1:
            w_q = deque(wheel[index+1])
            w_q.append(w_q.popleft())
            w_q = list(w_q)
            wheel[index+1] = w_q
        

for index, w in enumerate(wheel[1:]):
    if w[0] == 1:
        answer += 2**index
print(answer)