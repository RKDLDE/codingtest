def solution(n):
    even, odd = 0, 0
    for i in range(1, n+1):
        if i % 2 == 0:
            odd = i * i + odd
        else:
            even += i
    return even if n % 2 != 0 else odd