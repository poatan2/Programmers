def solution(k, m, score):
    answer = 0
    
    score.sort() # 오름차순 정렬
    cnt_box = 0 # 상자에 들어간 사과의 게수
    tmp =[] # 상자
    
    while score:
        tmp.append(score.pop())
        cnt_box += 1
        
        if cnt_box == m:    # 상자가 꽉차면
            answer+= tmp.pop()*m # 가장 점수가 낮은 사과 pop해서 가격+
            cnt_box = 0
        
    
    
    return answer