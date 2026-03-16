def solution(dots):
    # x를 기준으로 정렬
    dots.sort(key=lambda x:x[0])
    y = abs(dots[0][1]-dots[1][1])
    
    # y를 기준으로 정렬
    dots.sort(key=lambda x:x[1])
    x = abs(dots[0][0]-dots[1][0])

    return x*y