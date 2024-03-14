string = input()
length = len(string)
R = 0
C = 0
# 최대 100글자이니 1부터 글자 길이까지 반복문 돌려서 최대 R값 찾기
for n in range(1, length):
    if length % n == 0:
        r = n
        c = length // n
        # R은 C 이하여야하니 이러한 경우 나오면 바로 break
        if r > c:
            break
        R = r
        C = c

#원래 정인이가 만든 행렬 형식으로 string에 입력 받은 것 matrix에 저장
matrix = [[''] * C for _ in range(R)]
for i, s in enumerate(string):
    row = i % R
    col = i // R
    matrix[row][col] = s

# 행 순서로 matrix 읽음
for row in range(R):
    for col in range(C):
        print(matrix[row][col], end="")