def solution(numLog):
    answer = ''
    for i in range(len(numLog)-1):
        diff = abs(numLog[i] - numLog[i+1])
        if diff == 1:
            if numLog[i] > numLog[i+1]:
                answer += "s"
            else:
                answer += "w"

        elif diff == 10:
            if numLog[i] > numLog[i+1]:
                answer += "a"
            else:
                answer += "d"

    return answer