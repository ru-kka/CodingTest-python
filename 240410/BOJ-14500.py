import sys
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = []
for _ in range(N):
    l = [int(num) for num in input().split()]
    matrix.append(l)

answer_list = []
for i in range(N):
    for j in range(M):
        if (j+3)<M:
            candidate = matrix[i][j] + matrix[i][j+1] + matrix[i][j+2] + matrix[i][j+3]
            answer_list.append(candidate)

        if (i+3)<N:
            candidate = matrix[i][j] + matrix[i+1][j] + matrix[i+2][j] + matrix[i+3][j]
            answer_list.append(candidate)
        
        if (i+2)<N and (j+1)<M:
            candidate1 = matrix[i][j] + matrix[i+1][j] + matrix[i+2][j] + matrix[i][j+1]
            candidate2 = matrix[i][j] + matrix[i+1][j] + matrix[i+2][j] + matrix[i+1][j+1]
            candidate3 = matrix[i][j] + matrix[i+1][j] + matrix[i+2][j] + matrix[i+2][j+1]
            candidate4 = matrix[i][j] + matrix[i+1][j] + matrix[i+1][j+1] + matrix[i+2][j+1]
            answer_list.append(candidate1)
            answer_list.append(candidate2)
            answer_list.append(candidate3)
            answer_list.append(candidate4)
        
        if (i+2)<N and 0<=(j-1):
            candidate1 = matrix[i][j] + matrix[i+1][j] + matrix[i+2][j] + matrix[i][j-1]
            candidate2 = matrix[i][j] + matrix[i+1][j] + matrix[i+2][j] + matrix[i+1][j-1]
            candidate3 = matrix[i][j] + matrix[i+1][j] + matrix[i+2][j] + matrix[i+2][j-1]
            candidate4 = matrix[i][j] + matrix[i+1][j] + matrix[i+1][j-1] + matrix[i+2][j-1]
            answer_list.append(candidate1)
            answer_list.append(candidate2)
            answer_list.append(candidate3)
            answer_list.append(candidate4)
        
        if (i+1)<N and (j+2)<M:
            candidate1 = matrix[i][j] + matrix[i][j+1] + matrix[i][j+2] + matrix[i+1][j]
            candidate2 = matrix[i][j] + matrix[i][j+1] + matrix[i][j+2] + matrix[i+1][j+1]
            candidate3 = matrix[i][j] + matrix[i][j+1] + matrix[i][j+2] + matrix[i+1][j+2]
            candidate4 = matrix[i][j] + matrix[i][j+1] + matrix[i+1][j+1] + matrix[i+1][j+2]
            answer_list.append(candidate1)
            answer_list.append(candidate2)
            answer_list.append(candidate3)
            answer_list.append(candidate4)

        if 0<=(i-1) and (j+2)<M:
            candidate1 = matrix[i][j] + matrix[i][j+1] + matrix[i][j+2] + matrix[i-1][j]
            candidate2 = matrix[i][j] + matrix[i][j+1] + matrix[i][j+2] + matrix[i-1][j+1]
            candidate3 = matrix[i][j] + matrix[i][j+1] + matrix[i][j+2] + matrix[i-1][j+2]
            candidate4 = matrix[i][j] + matrix[i][j+1] + matrix[i-1][j+1] + matrix[i-1][j+2]
            answer_list.append(candidate1)
            answer_list.append(candidate2)
            answer_list.append(candidate3)
            answer_list.append(candidate4)
        
        if (i+1)<N and (j+1)<M:
            candidate = matrix[i][j] + matrix[i+1][j] + matrix[i][j+1] + matrix[i+1][j+1]
            answer_list.append(candidate)

print(max(answer_list))