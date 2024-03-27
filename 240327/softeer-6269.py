M, N, K = map(int, input().split())

secret_number = [int(num) for num in input().split()]
user_number = [int(num) for num in input().split()]

flag = False
for i in range(0,N-M+1):
    cnt = 0
    for j in range(0,M):
        if secret_number[j] == user_number[i+j]:
            cnt += 1
        else:
            break
    if cnt == M:
        flag = True

if flag == True:
    print("secret")
else:
    print("normal")