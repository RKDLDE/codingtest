def solution(number):
    number = list(map(int, number))
    return sum(number) % 9
    