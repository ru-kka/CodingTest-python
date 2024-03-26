string = input()

answer = 0
for s in string:
    if s == " ":
        answer += 1

if string[0] == " ":
    answer -= 1
if string[-1] == " ":
    answer -= 1

print(answer + 1)