from itertools import permutations

N, M, K = map(int, input().split())
weight = [int(num) for num in input().split()]

w_com = list(permutations(weight))

answer = 10**10
for w in w_com:
    index = 0
    candidate = 0
    for i in range(K):
        sum = 0
        while sum + w[index] <= M:
            sum += w[index]
            index += 1
            index = index % N
        candidate += sum
    answer = min(answer, candidate)

print(answer)