import sys
input = sys.stdin.readline

r, c, k = map(int, input().split())
r -= 1
c -= 1

matrix = [[0]*100 for _ in range(100)]
for x in range(3):
    for y, num in enumerate(input().split()):
        matrix[x][y] = int(num)
row_max = 2
col_max = 2

answer = 0
while matrix[r][c] != k:
    if row_max >= col_max:
        ncol_max = 0
        for row in range(row_max+1):
            my_dic = {}
            for r_num in matrix[row]:
                if r_num == 0:
                    continue
                else:
                    if r_num in my_dic.keys():
                        my_dic[r_num] += 1
                    else:
                        my_dic[r_num] = 1
            my_dic = sorted(my_dic.items(), key=lambda x:(x[1], x[0]))
            position = 0
            for key, item in my_dic:
                if position == 100:
                    break
                matrix[row][position] = key
                position += 1
                matrix[row][position] = item
                position += 1
            for col in range(position, 100):
                matrix[row][col] = 0
            ncol_max = max(ncol_max, position-1)
        col_max = ncol_max
    else:
        nrow_max = 0
        for col in range(col_max+1):
            my_dic = {}
            for row in range(row_max+1):
                if matrix[row][col] == 0:
                    continue
                else:
                    if matrix[row][col] in my_dic.keys():
                        my_dic[matrix[row][col]] += 1
                    else:
                        my_dic[matrix[row][col]] = 1
            my_dic = sorted(my_dic.items(), key=lambda x:(x[1], x[0]))
            position = 0
            for key, item in my_dic:
                if position == 100:
                    break
                matrix[position][col] = key
                position += 1
                matrix[position][col] = item
                position += 1
            for row in range(position, 100):
                matrix[row][col] = 0
            nrow_max = max(nrow_max, position-1)
        row_max = nrow_max
    answer += 1
    if answer > 100:
        answer = -1
        break
print(answer)