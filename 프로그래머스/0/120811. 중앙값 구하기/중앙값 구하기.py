def solution(array):
    array = sorted(array)
    n = len(array)
    
    if n % 2 == 1:
        return array[n//2]
    else:
        return (array[n//2-1] + array[n//2])//2