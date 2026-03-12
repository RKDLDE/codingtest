def solution(emergency):
    answer = []
    s_e = sorted(emergency, reverse=True)
    for i in emergency:
        answer.append(s_e.index(i)+1)
    return answer