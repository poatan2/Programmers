def solution(n):
    answer = 0
    num = 1
    
    while num<n :
        if n//num != num:
            num+=1
        else:
            break
    
    if n/num == num:
        return (num+1)**2

    return -1