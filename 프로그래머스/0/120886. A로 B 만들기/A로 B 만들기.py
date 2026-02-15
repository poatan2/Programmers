def solution(before, after):
    answer = 0
    
    for i in before:
        for j in after:
            if i == j:
                before = before.replace(i,"",1)
                after = after.replace(j,"",1)
                
    if before =="" and after=="":
        answer = 1
    else:
        answer = 0
    
    return answer