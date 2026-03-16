def solution(id_pw, db):
    result = ''
    for i in db:
        if id_pw[0] == i[0] and id_pw[1] == i[1]:
            result = "login"
            break
        elif id_pw[0] == i[0] and id_pw[1] != i[1]:
            result = "wrong pw"
            break
        else:
            result = "fail"
    return result