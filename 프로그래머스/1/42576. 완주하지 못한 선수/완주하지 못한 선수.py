def solution(participant, completion):
    answer = ''
    
    participant.sort()
    completion.sort()
    
    for i in range(len(participant)):
        if i == len(participant)-1:     # 마지막 인덱스라면 완주하지 못한 사람이다.
            answer = participant[i]     
            break
        elif participant[i] != completion[i]:
            answer = participant[i]
            break
            
    return answer