def solution(my_str, n):
    answer = []
    temp = ''
    cnt = 0
    
    
    for i in my_str:
        temp += i
        cnt +=1
        if cnt == n:
            answer.append(temp)
            temp = ''
            cnt = 0
        
    if temp != '':
        answer.append(temp)    
    
    return answer