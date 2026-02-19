def solution(arr):
    answer = []
    
    # 배열에서의 최솟값 구하기
    min_value = min(arr)
    
    # 최솟값 제외하고 배열 채우기
    for i in arr:
        if i != min_value:
            answer.append(i)
    
    # 만약 배열이 비어있으면 -1 넣기
    if len(answer) == 0:
        answer.append(-1)
    
    
    return answer