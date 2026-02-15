def solution(board):
    answer = 0
    n = len(board) # 1차원 배열이 몇개 들어있는지

    # danger_map = board => 이 코드는 나쁜 코드다
    # 이렇게 하면 둘이 같은 리스트를 가리키게 된다.
    # 따라서 내가 1로 체크한 것이 공유된다. 

    # 올바른 2차원 리스트 초기화 방식
    # 새로운 지뢰지도를 만든다. (여기에 위험지역을 표시할 것이다.)
    danger_map = [[0] * n for _ in range(n)]
    
    # 아래 배열은 위험지역으로 표시될 좌표이다.
    # 예를 들어 [3][2] 인덱스에 지뢰가 있다면
    # 주변 지역 [2][1],[2][2],[2][3] ~~~~ [4][3] 까지가 위험지역이다.
    # 이것은 일정한 패턴을 가지므로 그 위치를 나중에 계산하도록 하기 위한 배열이다.
    dr = [-1,-1,-1,0,0,1,1,1] # 행
    dc = [-1,0,1,-1,1,-1,0,1] # 열

    # 핵심 로직
    for i in range(n):
        for j in range(n):
            # 1. 지뢰의 위치를 찾는다.
            if board[i][j] == 1:
                # 지뢰위치 표시
                danger_map[i][j] =1 
                # 2. 위험지역을 찾는다.
                for k in range(8):  
                    mapLow = i + dr[k] # 이 과정으로 위험지역의 위치를 계산
                    mapCol = j + dc[k]
                    
                    # 지도를 벗어났는지 계산한다.
                    if 0 <= mapLow < n and 0 <= mapCol < n:
                        danger_map[mapLow][mapCol]= 1
                

    cnt = 0
    # 3. 위험지역을 제외한 영역을 계산한다.
    for i in range(n):
        for j in range(n):
            if danger_map[i][j]==0:
                cnt+=1
    
    answer = cnt
    
    return answer