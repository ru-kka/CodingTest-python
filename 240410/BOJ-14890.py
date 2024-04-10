import sys
input = sys.stdin.readline

N, L = map(int, input().split())
matrix = []
for _ in range(N):
    l = [int(num) for num in input().split()]
    matrix.append(l)

answer = 0
# 행 살펴보기
for r in range(N):
    flag = True
    # 0은 경사로를 놓은 적 없는 곳
    visited =[0]*N
    for c in range(N-1):
        if matrix[r][c] < matrix[r][c+1]:
            if matrix[r][c] + 1 < matrix[r][c+1]:
                flag = False
                break
            else:
                height = matrix[r][c]
                if visited[c] == 1:
                    flag = False
                    break
                visited[c] = 1
                for i in range(1,L):
                    if 0<=(c-i) and matrix[r][c-i] == height and visited[c-i] == 0:
                        visited[c-i] = 1
                        continue
                    else:
                        flag = False
                        break

        elif matrix[r][c] > matrix[r][c+1]:
            if matrix[r][c] > matrix[r][c+1] + 1:
                flag = False
                break
            else:
                height = matrix[r][c+1]
                visited[c+1] = 1
                for i in range(1, L):
                    if (c+1+i)<N and matrix[r][c+1+i] == height and visited[c+1+i] == 0:
                        visited[c+1+i] = 1
                        continue
                    else:
                        flag = False
                        break
        
        if flag:
            continue
        else:
            break
    if flag:
        answer += 1

# 열 살펴보기
for c in range(N):
    flag = True
    # 0은 경사로를 놓은 적 없는 곳
    visited =[0]*N
    for r in range(N-1):
        if matrix[r][c] < matrix[r+1][c]:
            if matrix[r][c] + 1 < matrix[r+1][c]:
                flag = False
                break
            else:
                height = matrix[r][c]
                if visited[r] == 1:
                    flag = False
                    break
                visited[r] = 1
                for i in range(1,L):
                    if 0<=(r-i) and matrix[r-i][c] == height and visited[r-i] == 0:
                        visited[r-i] = 1
                        continue
                    else:
                        flag = False
                        break

        elif matrix[r][c] > matrix[r+1][c]:
            if matrix[r][c] > matrix[r+1][c] + 1:
                flag = False
                break
            else:
                height = matrix[r+1][c]
                visited[r+1] = 1
                for i in range(1, L):
                    if (r+1+i)<N and matrix[r+1+i][c] == height and visited[r+1+i] == 0:
                        visited[r+1+i] = 1
                        continue
                    else:
                        flag = False
                        break
        
        if flag:
            continue
        else:
            break
    if flag:
        answer += 1
print(answer)