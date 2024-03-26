answer = 0
for _ in range(5):
    start, finish = map(str, input().split())
    
    start_hour = int(start[:2])
    start_minute =int(start[3:])
    finish_hour = int(finish[:2])
    finish_minute =int(finish[3:])

    if start_minute > finish_minute:
        answer += (finish_hour - start_hour - 1) * 60
        answer += (60+finish_minute - start_minute)
    else:
        answer += (finish_hour - start_hour) * 60
        answer += finish_minute - start_minute

print(answer)