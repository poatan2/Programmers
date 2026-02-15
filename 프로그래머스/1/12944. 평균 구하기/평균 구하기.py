def solution(arr):
    answer = 0
    sum = 0
    n = len(arr)
    
    for i in range(n):
        sum += arr[i]
        
    answer = sum/n
    
    return answer