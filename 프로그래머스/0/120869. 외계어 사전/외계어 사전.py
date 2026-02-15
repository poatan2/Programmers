def solution(spell, dic):
    answer = 0
    # spell로 조립할 수 있는 모든 단어를 만든다.
    # 그리고 그것이 dic에 있는지 검사한다.
    
    
    # 근데 이것보다 하나씩 spell에서 지워가면 되는거 아님??
    # 그니까 zdx인데 dzx면 d 지우고 z 지워지고, x 지워지면서 spell이 비어지면 통과
    
    temp = list(spell)
    
    for word in dic:
        for wordSpell in word:
            for abet in spell:
                if wordSpell == abet:
                    spell.remove(wordSpell)
                    #print(spell)
        if not spell:
            answer = 1
        else:
            # spell = temp =>이렇게 하면 메모리 상의 똑같은 리스트를 가리키게 됨
            # 따라서 이후부터 temp도 영향을 받게 된다.
            spell = list(temp)
            answer = 2
            
    return answer