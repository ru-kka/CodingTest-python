import sys
input = sys.stdin.readline

myList = []


def myInsert(pos, value):
    global myList

    if pos == 0:
        myList = [value] + myList
    elif pos == 1:
        
        myList = myList + [value]


def myErase(pos, value):
    global myList

    if pos == 0:
        cnt = 0
        myNewList = []
        for index, num in enumerate(myList):
            if cnt >= 3:
                myNewList = myNewList + myList[index:]
                break
            if num < value:
                myNewList.append(num)
            else:
                cnt += 1
        myList = myNewList
    elif pos == 1:
        cnt = 0
        reverseList = myList[::-1]
        myNewList = []
        for index, num in enumerate(reverseList):
            if cnt >= 3:
                myNewList = myNewList + reverseList[index:]
                break
            if num < value:
                myNewList.append(num)
            else:
                cnt += 1
        myList = myNewList[::-1]


def mySort(value):
    global myList

    myList = sorted(myList, key=lambda x:(abs(value-x), x))


def myPrint(pos):
    global myList

    if pos == 0:
        print(*myList)
    elif pos == 1:
        print(*myList[::-1])


if __name__ == "__main__":
    q = int(input())
    for _ in range(q):
        cmd = list(map(int, input().split()))

        if cmd[0] == 1:
            myInsert(cmd[1], cmd[2])
        elif cmd[0] == 2:
            myErase(cmd[1], cmd[2])
        elif cmd[0] == 3:
            mySort(cmd[1])
        elif cmd[0] == 4:
            myPrint(cmd[1])
