def solution(strings, n):
    answer = []
    
    # n 위치의 문자가 같을 경우 사전순 정렬이니까
    # 미리 정렬해놓기
    strings.sort()
    
    # 버블 정렬
    for i in range(len(strings)-1):
        for j in range(len(strings)-1-i):
            if strings[j][n]>strings[j+1][n]:
                temp = strings[j]
                strings[j] = strings[j+1]
                strings[j+1] = temp
            
    answer=strings
        
    return answer