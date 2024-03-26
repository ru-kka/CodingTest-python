N = int(input())
score = [int(num) for num in input().split()]

M = max(score)

for index, s in enumerate(score):
    score[index] = (s/M) * 100

answer = sum(score) / N
print(answer)