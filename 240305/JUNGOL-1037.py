N = int(input())
matrix = []
for _ in range(0, N):
    matrix.append([int(num) for num in input().split()])

# 행, 열 각각 1의 개수 저장하는 배열 생성
row = [0] * N
col = [0] * N
for r in range(N):
    for c in range(N):
        if matrix[r][c] == 1:
            row[r] += 1
            col[c] += 1

# 행, 열 이상있는 index 저장하기 위한 list 생성
row_p = []
col_p = []
# row, col 각각 1의 개수 확인하여 이상 있는 index check
for index, r in enumerate(row):
    if r % 2 == 1:
        row_p.append(index)
for index, c in enumerate(col):
    if c % 2 == 1:
        col_p.append(index)

# row, col 모두 이상 없으면 OK 출력
if not row_p and not col_p:
    print('OK')
# row, col 각각 이상 있는 것 1개씩 있을 경우 아래와 같이 출력
elif len(row_p) == 1 and len(col_p) == 1:
    print('Change bit (' + str(row_p[0]+1) + ',' + str(col_p[0]+1) + ')')
else:
    print('Corrupt')