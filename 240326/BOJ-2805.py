N, M = map(int, input().split())
tree = [int(num) for num in input().split()]

left = 0
right = max(tree)

answer = 0
candidate = 0
find = False
while left <= right:
    target = (left + right) // 2

    length = 0
    for t in tree:
        if t > target:
            length += (t - target)
    
    if length < M:
        right = target - 1
    elif length > M:
        left = target + 1
        candidate = target
    elif length == M:
        answer = target
        find = True
        break

if find == True:
    print(answer)
else:
    print(candidate)