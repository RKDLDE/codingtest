def solution(my_string, indices):
    answer = ''
    for idx, value in enumerate(my_string):
        if idx in indices:
            continue
        else:
            answer += value
    return answer