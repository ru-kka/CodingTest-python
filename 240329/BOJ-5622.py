import sys
input = sys.stdin.readline

alpha_list = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

string = input().rstrip()

answer = 0
for s in string:
    for index, l in enumerate(alpha_list):
        if s in l:
            answer += index+3

print(answer)