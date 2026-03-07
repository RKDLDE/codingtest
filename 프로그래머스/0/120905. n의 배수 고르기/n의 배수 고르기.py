def solution(n, numlist):
    numlist2 = []
    
    for i in numlist:
        if i % n == 0:
            numlist2.append(i)
    
    return numlist2