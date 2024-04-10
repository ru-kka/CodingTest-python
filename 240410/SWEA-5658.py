from collections import deque

alpha = ['A', 'B', 'C', 'D', 'E', 'F']

T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())

    number_string_list = deque([])
    number_string = input()
    for n in number_string:
        number_string_list.append(n)
    
    generate_number = set([])
    cnt = 0
    while cnt < N//4:
        for i in range(4):
            start = (N//4)*i
            end = (N//4)*(i+1)
            nsl_part = list(number_string_list)[start:end]
            number = 0
            for j in range(N//4):
                if (nsl_part[j]).isdigit():
                    number += int(nsl_part[j])*(16**(N//4-1-j))
                else:
                    index = alpha.index(nsl_part[j])
                    number += (10+index)*(16**(N//4-1-j))
            generate_number.add(number)

        n = number_string_list.popleft()
        number_string_list.append(n)
        cnt += 1
    
    generate_number = list(generate_number)
    generate_number = sorted(generate_number, reverse=True)

    print('#{0} {1}'.format(test_case, generate_number[K-1]))