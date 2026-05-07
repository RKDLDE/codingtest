def tenton(n, q):
    rev_base = ''
    
    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)
        
    return rev_base[::]
    
def solution(n):
    answer = tenton(n, 3)
    print(answer)
    return int(answer, 3)