import sys
input = sys.stdin.readline

N = int(input())
number = []
_sum = 0
count = dict()
for _ in range(N):
    n = int(input())
    number.append(n)
    _sum += n

    if n not in count:
        count[n] = 1
    else:
        count[n] += 1

number = sorted(number, key=lambda x:x)

print(round(_sum / N))
print(number[N//2])

freq = max(count.values())
max_list = []
for key, value in count.items():
    if value == freq:
        max_list.append(key)
if len(max_list) == 1:
    print(max_list[0])
else:
    max_list = sorted(max_list, key=lambda x:x)
    print(max_list[1])

print(number[-1] - number[0])