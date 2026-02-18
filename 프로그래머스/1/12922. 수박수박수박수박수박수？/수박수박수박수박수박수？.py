def solution(n):
    answer = ''
    cnt=1
    while cnt<=n:
        if cnt%2 == 1:
            answer+='수'
        else:
            answer+='박'
        cnt+=1
    
    return answer