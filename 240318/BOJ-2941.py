# 단순 구현
alpha = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']

s = input()
cnt = 0
while len(s) != 0:
    if len(s) == 1:
        cnt += 1
        break
    elif len(s) == 2:
        if s in alpha:
            cnt += 1
            break
        else:
            cnt += 2
            break
    elif len(s) == 3:
        if s == 'dz=':
            cnt += 1
            break
        if s[:2] in alpha:
            cnt += 1
            s = s[-1]
        else:
            cnt += 1
            s = s[-2:]
    else:
        if s[:3] == 'dz=':
            cnt += 1
            s = s[3:]
            continue
        if s[:2] in alpha:
            cnt += 1
            s = s[2:]
            continue
        cnt += 1
        s = s[1:]

print(cnt)