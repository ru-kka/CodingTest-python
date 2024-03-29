import sys
input = sys.stdin.readline

expression = input().rstrip()
number = []
cal_list = []
num = ''
for e in expression:
    if e.isdigit():
        num += e
    else:
        number.append(int(num))
        num = ''
        cal_list.append(e)
number.append(int(num))

# 몇번째 숫자를 다루는지 기억할 index
index = 1
# 정답으로 반환될 값
answer = number[0]
# - 상태를 check할 flag
flag = False
# - 상태에 keep해둘 값
keep = 0
for cal in cal_list:
    if cal == '+':
        if flag == False:
            answer += number[index]
        elif flag == True:
            keep += number[index]
    elif cal == '-':
        if flag == False:
            flag = True
            keep += number[index]
        elif flag == True:
            answer -= keep
            keep = 0
            keep += number[index]
    index += 1
if keep != 0:
    answer -= keep

print(answer)