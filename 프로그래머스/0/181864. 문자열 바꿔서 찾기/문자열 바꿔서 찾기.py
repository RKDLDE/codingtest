def solution(myString, pat):
    chString = ""
    for s in myString:
        if s == "A":
            chString += "B"
        else:
            chString += "A"
    
    return 1 if pat in chString else 0