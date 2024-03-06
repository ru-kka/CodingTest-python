K = int(input())

# 오른쪽, 아래 총 길이만 저장
right = []
down = []
# 각각 길이, 방향 따로 저장
length = [0] * 6
direction = [0] * 6
# 포인트가 되는 지정 따로 저장해둠
# 해당 지점 dif에 길이 저장
point = [[1,3], [4,1], [2, 4], [3, 2]]
dif = []
# 포인트에 해당되는 지점 찾았는지 여부 확인하는 flag
flag = False
for i in range(6):
    direction[i], length[i] = map(int, input().split())

    # 오른쪽, 아래 총 길이만 저장
    if direction[i] == 1:
        right.append(length[i])
    elif direction[i] == 3:
        down.append(length[i])
    
    # 첫번째 아닌 반복문 아닐 때 point 지점에 해당지점인지 확인
    if i > 0:
        if [direction[i-1], direction[i]] in point:
            dif.append(length[i-1])
            dif.append(length[i])
            flag = True

# 포인트가 되는 지점을 찾지 못했을 경우 아래와 같은 방법으로 포인트 찾음
if flag == False:
    dif.append(length[5])
    dif.append(length[0])
total_x = sum(right)
total_y = sum(down)
print((total_x * total_y - dif[0] * dif[1]) * K)