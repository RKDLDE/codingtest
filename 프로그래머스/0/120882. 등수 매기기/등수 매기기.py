def solution(score):
    answer = []
    
    # 이중 for
    for i in range(0, len(score)):
        # 비교 대상
        avgI = sum(score[i])/len(score[i])
        rank = 1
        
        # 나머지 원소들 비교
        for j in range(0, len(score)):
            # 본인은 건너뛰고
            if i == j:
                continue
            avgJ = sum(score[j])/len(score[j])
            
            # 본인보다 크면 rank에 +1
            if avgI < avgJ:
                rank += 1

        answer.append(rank)
    return answer