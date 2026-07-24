def solution(name, yearning, photo):
    answer = []
    
    # name을 key로 yearing을 value로 해서 dict를 만들기
    missing = {}
    cnt = 0
    
    for item in name: 
        missing[item] = yearning[cnt] # 딕셔너리 생성
        cnt+=1
        
    
    total = 0
    for i in photo: 
        for j in i:
            if j in missing:    
                total += missing[j]
        
        answer.append(total)
        total = 0
    
    return answer