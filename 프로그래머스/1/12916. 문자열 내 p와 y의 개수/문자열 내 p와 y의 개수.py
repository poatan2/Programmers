def solution(s):
    answer = True
    cnt_p = 0
    cnt_y = 0
    
    for i in s:
        if i=='p' or i=='P':
            cnt_p+=1
        if i=='y' or i=='Y':
            cnt_y+=1
    
    if cnt_p == 0 and cnt_y == 0:
        return True
    elif cnt_p == cnt_y:
        return True
    else:
        return False
    
    return True