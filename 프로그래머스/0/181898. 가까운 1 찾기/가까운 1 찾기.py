def solution(arr, idx):
    a = map(str, arr[idx:])
    new_arr = ''.join(a)
    return new_arr.find('1') + idx if new_arr.find('1') != -1 else -1