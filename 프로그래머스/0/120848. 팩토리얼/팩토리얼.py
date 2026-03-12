def solution(n):
    answer = 1
    j = 1
    while True:
        answer = 1
        for i in range(j, 1, -1):
            answer *= i
        if answer >= n:
            break
        j += 1

    return j-1 if answer > n else j