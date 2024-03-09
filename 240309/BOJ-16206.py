N, M = map(int, input().split())
cake = [int(num) for num in input().split()]

# mod 10 0인 것과 작은 것 순으로 정렬
cake = sorted(cake, key=lambda x : (x % 10,x))

answer = 0
for c in cake:
    # 길이 10이면 개수 1증가
    # 다음 반복문으로 진행
    if c == 10:
        answer += 1
        continue
    # 자를 수 있는 횟수 남아있고 케이크 길이 10보다 클 때까지 반복문 돌림
    while M > 0 and c > 10:
        M -= 1
        c -= 10
        answer += 1
    # 남은 케이크 길이 10이면 anwer에 1증가
    # 원래 mod 10 0인 케이크 의 경우 이렇게 증가
    # 20, 30, 40이 이런 예시임
    if c == 10:
        answer += 1
    
    if M == 0:
        break
print(answer)