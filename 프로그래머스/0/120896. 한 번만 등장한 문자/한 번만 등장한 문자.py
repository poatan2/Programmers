def solution(s):
    answer = ''
       
    cnt = 0
    for i in s:
        for j in s:
            if (i==j):
                cnt +=1
        if cnt ==1:
            answer +=i
        cnt=0
    
    answer = ''.join(sorted(answer))
    return answer