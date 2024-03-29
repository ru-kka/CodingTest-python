import sys
input = sys.stdin.readline

N = int(input())
serial_len = [[] for _ in range(51)]
max_length = 0
for _ in range(N):
    string = input().rstrip()
    number = 0
    for s in string:
        if s.isdigit():
            number += int(s)
    serial_len[len(string)].append([string, number])
    max_length = max(max_length, len(string))

answer = []
for serial_part in serial_len[1:max_length+1]:
    if serial_part:
        serial_part = sorted(serial_part, key=lambda x:(x[1], x[0]))
        for serial in serial_part:
            answer.append(serial[0])

for a in answer:
    print(a)

# 이렇게 한번에 sort하게 하는 것이 가장 좋음
# arr.sort(key = lambda x:(len(x), sum_num(x), x))