N = int(input())
switch = [0]
for num in input().split():
    switch.append(int(num))

def switch_number(num):
    if switch[num] == 0:
        switch[num] = 1
    elif switch[num] == 1:
        switch[num] = 0

M = int(input())
for _ in range(M):
    sex, number = map(int, input().split())
    if sex == 1:
        for multiple in range(1, N//number + 1):
            switch_number(number * multiple)
    elif sex == 2:
        switch_number(number)
        left = number - 1
        right = number + 1
        while left >= 1 and right <= N:
            if switch[left] == switch[right]:
                switch_number(left)
                switch_number(right)
                left -= 1
                right += 1
            else:
                break

cnt = 0
for s in switch[1:]:
    print(s, end=" ")
    cnt += 1
    if cnt % 20 == 0:
        print()