def solution(babbling):
    answer = 0
    
    zoka = ["aya","ye","woo","ma"]
    
    
    for word in babbling:
        for z in zoka: # 단어를 하나씩 가져와 검사한다.
            if z in word:
                # 이때 있는 단어를 띄어쓰기로 바꿔준다.
                # 왜냐?, wyeoo를 보고 ye가 있다. 만약 공백이 아니라 ""로 변환하면 woo가 된다
                # 이것은 이어 붙인 조합이 아니므로 공백을 처리하여 woo로 만들어지지 않게 해야 한다.
                word = word.replace(z, " ")
                
        if word.strip() == "": # 그리고 마지막에 띄어쓰기를 제거하여 검사한다.
            answer+=1
    
    
    
    return answer




solution(["aya", "yee", "u", "maa", "wyeoo"])