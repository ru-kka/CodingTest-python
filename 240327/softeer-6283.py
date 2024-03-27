gear = [int(num) for num in input().split()]

asc = True
des = True
for index in range(7):
    if gear[index+1] - gear[index] != 1:
        asc = False

    if gear[index+1] - gear[index] != -1:
        des = False

if asc == True:
    print('ascending')
if des == True:
    print('descending')
if asc == des:
    print('mixed')