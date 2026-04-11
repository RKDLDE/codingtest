def solution(a, b):
    a_plus_b = int(str(a) + str(b))
    return a_plus_b if a_plus_b > 2 * a * b else 2 * a * b