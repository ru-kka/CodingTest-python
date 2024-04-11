from itertools import combinations
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int, input().split())

chicken = []
house = []
matrix = [[0] for _ in range(N+1)]
for r in range(1, N+1):
    for c, num in enumerate(input().split()):
        if int(num) == 2:
            chicken.append([r, c+1])
            matrix[r].append(0)
        elif int(num) == 1:
            house.append([r, c+1])
            matrix[r].append(1)
        else:
            matrix[r].append(int(num))

chicken_com = combinations(chicken, M)
min_chicken_distance = int(10e9)
for chicken_case in chicken_com:
    min_chicken_case_distance = 0
    for h in house:
        min_house_chicken = int(10e9)
        for c in chicken_case:
            min_house_chicken = min(min_house_chicken, abs(h[0] - c[0]) + abs(h[1] - c[1]))
        min_chicken_case_distance += min_house_chicken
    min_chicken_distance = min(min_chicken_distance, min_chicken_case_distance)
print(min_chicken_distance)