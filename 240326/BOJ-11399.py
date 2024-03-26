N = int(input())
time = [int(num) for num in input().split()]
time = sorted(time, key = lambda x: x)

total_time = []
accumulate = 0
for t in time:
    total_time.append(accumulate + t)
    accumulate += t

print(sum(total_time))