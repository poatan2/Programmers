def solution(s, skip, index):
    answer = ''
    
    new_alpha=[]
    cnt_alpha=26-len(skip)
    
    for i in range(97,123):
        if chr(i) not in skip:
            new_alpha.append(chr(i))
            
    for i in s:
        temp=(new_alpha.index(i)+index)%cnt_alpha
        answer+=new_alpha[temp]
    
    
    return answer