def solution(before, after):
    before = ''.join(sorted(list(before)))
    after = ''.join(sorted(list(after)))
    if before == after:
        return 1
    else:
        return 0