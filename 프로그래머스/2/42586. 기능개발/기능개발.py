def solution(progresses, speeds):
    answer = []

    #각 작업의 개발 기간을 저장하는 큐
    queue = []

    for i in range(len(progresses)):
        # 총 개발 기간을 계산
        cnt = 0
        dday = progresses[i]
        while dday<100:
            dday += speeds[i]
            cnt+=1
        queue.append(cnt)

    
    max_val = queue[0] # 큐의 첫 번째를 기준
    cnt_deploy = 1
    for i in queue[1:]:
        # 기준보다 작거나 같으면 같이 배포해야 하므로 +1
        if max_val >= i: 
            cnt_deploy+=1
        # 그게 아니라면 더 오래걸리니까 기준을 변경
        else:            
            answer.append(cnt_deploy)
            cnt_deploy = 1
            max_val = i

    answer.append(cnt_deploy)
        

    return answer