def solution(num_list):
    if len(num_list) >= 11:
        answer = sum(num_list)
    else:
        pow = 1
        for i in num_list:
            pow *= i
        answer = pow
    return answer