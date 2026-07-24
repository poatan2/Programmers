def solution(cards1, cards2, goal):
    answer = ''
    
    # del을 사용하면 리스트가 비어버려 out of index 에러가 발생한다.
    # 따라서 0번쨰 값을 뒤로 보내어 리스트가 비지 않도록 한다.
    for i in goal:
        if i == cards1[0]:
            # del cards1[0]  
            cards1.append(cards1.pop(0))
        elif i == cards2[0]:
            # del cards2[0]
            cards2.append(cards2.pop(0))
        else:
            return "No"
        
    return "Yes"