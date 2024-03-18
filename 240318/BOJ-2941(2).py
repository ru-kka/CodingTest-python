alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

s = input()

for a in alpha:
    # 입력받은 s에 alpha 요소 있으면 0으로 바꿈
    # 하나로 퉁친다고 생각하면 됨
    s = s.replace(a, "0")

print(len(s))