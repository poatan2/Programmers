def solution(array):
    answer = 0
    s=''
    for i in array:
        s+= str(i)
    
    for j in s:
        if int(j) == 7:
            answer+=1
    
    return answer