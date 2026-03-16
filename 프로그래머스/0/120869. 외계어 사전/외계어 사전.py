def solution(spell, dic):
    answer = 0
    for i in  dic:
        flag = 0
        for j in spell:
            if j in i:
                flag += 1
        if flag == len(spell):
            answer += 1
    return 1 if answer else 2