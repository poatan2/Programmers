def solution(n):
    answer = []
    
    temp = str(n)
    
    for i in range(len(temp)-1,-1,-1):
        answer.append(int(temp[i]))
    
    
    return answer