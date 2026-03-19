def solution(sizes):
    answer = 0
    temp = 0 
    result=[]
    
    # 모든 명함을 w>h가 되게 정렬
    # 가로 ,세로 길이 중 각각 가장 큰 길이를 선택하면 됨
    
    # w>h로 정렬
    for i in range(0,len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            temp = sizes[i][0]
            sizes[i][0] = sizes[i][1]
            sizes[i][1] = temp
    
    # 각각 가장 큰 w,h를 찾기
    max_w = 0
    max_h = 0
    for i in range(0,len(sizes)):
        if max_w < sizes[i][0]:
            max_w = sizes[i][0]
        if max_h < sizes[i][1]:
            max_h = sizes[i][1]
    
    answer = max_w * max_h
    return answer