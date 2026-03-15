def solution(numbers, k):
    answer = 0
    return numbers[(k*2-2)%len(numbers)]
