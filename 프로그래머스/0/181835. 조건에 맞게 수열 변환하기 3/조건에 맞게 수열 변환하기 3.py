def solution(arr, k):
    arr_mul_k = list(map(lambda x: x * k, arr))
    arr_plus_k = list(map(lambda x: x + k, arr))
    return arr_mul_k if k % 2 != 0 else arr_plus_k