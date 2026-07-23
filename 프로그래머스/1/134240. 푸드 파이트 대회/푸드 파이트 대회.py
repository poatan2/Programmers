def solution(food):
    answer = ''
    
    foodok = [x//2 for x in food]
    
    # 왼쪽 사람 먹는 순서
    for i in range(1, len(foodok)):
        answer += str(i)*foodok[i]
        
    
    # 중간 물 삽입
    answer +='0'
    
    # 오른쪽 사람 먹는 순서
    for j in range(len(foodok)-1,0,-1):
        answer += str(j)*foodok[j]
    
    
    return answer