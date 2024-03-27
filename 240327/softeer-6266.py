N, M = map(int, input().split())

name = []
for _ in range(N):
    name.append(input())
name = sorted(name, key=lambda x:x)

time = [[True] * (9) for _ in range(N)]
for _ in range(M):
    r, s, t = map(str, input().split())

    i = name.index(r)
    for h in range(int(s), int(t)):
        time[i][int(h)-9] = False

answer = []
for t in time:
    room = []
    flag = False
    begin = 0
    for i in range(9):
        if t[i] == True:
            if flag == False:
                flag = True
                begin = i+9
                if i == 8:
                    room.append([begin, 18])
            elif flag == True:
                if i == 8:
                    room.append([begin, 18])
        elif t[i] == False:
            if flag == False:
                continue
            elif flag == True:
                flag = False
                room.append([begin, i+9])
    answer.append(room)

for i in range(1, N+1):
    print('Room {0}:'.format(name[i-1]))
    if not answer[i-1]:
        print('Not available')
    else:
        print('{0} available:'.format(len(answer[i-1])))
        for a in answer[i-1]:
            string = ''
            if a[0] == 9:
                string += str('09')
            else:
                string += str(a[0])
            string += '-'
            string += str(a[1])
            print(string)
    if i != N:
        print('-----')