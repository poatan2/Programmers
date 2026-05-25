def solution(arr1, arr2):
    row = len(arr1) #행의 길이
    col = len(arr1[0]) #열의 길이
    
    # 2차원 배열 정의하기
    answer = [[0 for _ in range(col)] for _ in range(row)]

    for i in range(0,row):
        for j in range(0,col):
            answer[i][j] = arr1[i][j]+arr2[i][j]
            
    
    return answer