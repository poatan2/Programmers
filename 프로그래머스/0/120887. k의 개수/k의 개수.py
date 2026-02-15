def solution(i, j, k):
    answer = 0
    s=''
    for i in range (i, j+1):
        s +=str(i)
    
    
    for x in s:
        if x==str(k):
            answer+= 1
            
    return answer