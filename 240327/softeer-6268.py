number = []
number.append([1, 1, 1, 0, 1, 1, 1]) # 0
number.append([0, 0, 1, 0, 0, 0, 1]) # 1
number.append([1, 0, 1, 1, 1, 1, 0]) # 2
number.append([1, 0, 1, 1, 0, 1, 1]) # 3
number.append([0, 1, 1, 1, 0, 0, 1]) # 4
number.append([1, 1, 0, 1, 0, 1, 1]) # 5
number.append([1, 1, 0, 1, 1, 1, 1]) # 6
number.append([1, 1, 1, 0, 0, 0, 1]) # 7
number.append([1, 1, 1, 1, 1, 1, 1]) # 8
number.append([1, 1, 1, 1, 0, 1, 1]) # 9

T = int(input())
for _ in range(T):
    A, B = map(str, input().split())

    answer = 0
    if len(A) == len(B):
        for position in range(0, len(A)):
            for i in range(7):
                if number[int(A[position])][i] != number[int(B[position])][i]:
                    answer += 1
                    
    elif len(A) > len(B):
        for position in range(0, len(A) - len(B)):
            for i in range(7):
                if number[int(A[position])][i] == 1:
                    answer += 1
        A = A[len(A) - len(B):]
        for position in range(len(B)):
            for i in range(7):
                if number[int(A[position])][i] != number[int(B[position])][i]:
                    answer += 1

    elif len(A) < len(B):
        for position in range(0, len(B) - len(A)):
            for i in range(7):
                if number[int(B[position])][i] == 1:
                    answer += 1
        B = B[len(B) - len(A):]
        for position in range(len(A)):
            for i in range(7):
                if number[int(A[position])][i] != number[int(B[position])][i]:
                    answer += 1

    print(answer)