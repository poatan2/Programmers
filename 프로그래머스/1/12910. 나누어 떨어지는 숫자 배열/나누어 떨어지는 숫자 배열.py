def solution(arr, divisor):
    answer = []
    
    for i in range(0,len(arr)):
        if (arr[i] % divisor) == 0:
            answer.append(arr[i])
    
    if not answer:  # answer 배열이 비어있다면
        answer.append(-1)
        return answer
    
    answer = sorted(answer)
    
    return answer