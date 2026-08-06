def solution(keymap, targets):
    answer = []
    cnt=0
    
    keymap_dict={}
    
    # keymap의 문자들을 dict로 만들기
    # 문자 : 최소위치
    for i in keymap:
        for idx in i:
            if idx in keymap_dict:
                if keymap_dict[idx] > i.index(idx)+1:
                    keymap_dict[idx] = i.index(idx)+1
            else:
                keymap_dict[idx] = i.index(idx)+1
    """
       str.index() 함수는 해당 리스트에서 그 문자가 가장 먼저 나온 위치를 반환
       
    """
    
    for target in targets:
        for idx in target:
            if idx in keymap_dict:
                cnt += keymap_dict[idx]
            else:
                cnt = -1
                break
                
        answer.append(cnt)
        cnt=0   
    
    return answer