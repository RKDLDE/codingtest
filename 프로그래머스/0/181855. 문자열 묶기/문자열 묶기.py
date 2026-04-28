from collections import Counter

def solution(strArr):
    a = [len(s) for s in strArr]
    num = Counter(a).most_common()
    return num[0][1]