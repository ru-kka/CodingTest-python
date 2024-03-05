N, L = map(int, input().split())
fruit = [int(num) for num in input().split()]

# 문제 조건따라 작성
while len(fruit) > 0:
    if min(fruit) <= L:
        fruit.remove(min(fruit))
        L += 1
    else:
        break

print(L)