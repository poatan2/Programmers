def solution(n):
    answer = 0
    result = 0
    
    
    for num in range(1,n+1):
        result = 0
        for i in range(num,n+1):
            result += i
            if result == n:
                answer+=1
                break
            if result > n:
                break
            

    return answer