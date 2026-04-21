def solution(myString):
    #myString = myString.replace("x","")
    
    answer = myString.split("x")
    answer = sorted(answer)
    
    result = []
    for i in answer:
        if i == '':
            continue
        else:
            result.append(i)
    
    return result
    