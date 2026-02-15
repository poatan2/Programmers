def solution(common):
    answer = 0
    
    n = len(common)
    
    # 두번째 - 첫번째 = 세번째 - 두번째 라면 등차수열
    if common[1]-common[0] == common[2]-common[1]:
        return common[-1]+common[1]-common[0]
    # 아니라면 등비수열이다.
    else:
        return common[-1]*(common[1]/common[0])