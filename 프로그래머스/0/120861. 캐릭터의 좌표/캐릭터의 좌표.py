def solution(keyinput, board):
    answer = []
    
    # right up 경계(양수)
    border1 = []
    border1.append(board[0] // 2)  
    border1.append(board[1] // 2)  
    
    # left, down 경계 (음수)
    border2 =[]
    border2.append(-border1[0])
    border2.append(-border1[1])
    
    # 초기위치 0,0
    loca = [0,0]
    
    # 경계를 벗어나는지를 함께 검사
    for dir in keyinput:
        if dir == 'left' and loca[0] > border2[0]:
            loca[0] = loca[0]-1
        elif dir =='right' and loca[0] < border1[0]:
            loca[0] = loca[0]+1
        elif dir == 'up' and loca[1] <border1[1]:
            loca[1] = loca[1] +1
        elif dir == 'down' and loca[1] > border2[1]:
            loca[1] = loca[1] -1
    
    answer = loca
    
    return answer