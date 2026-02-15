def solution(score):
    answer = []

    avg=[]
    
    # 평균 점수를 구한다.
    for i in range(len(score)):
        avg.append((score[i][0]+score[i][1]) / 2)

    # 새로운 리스트에 내림차순으로 정렬한다.
    arr = sorted(avg,reverse=True)
    # print(arr)

    # 새 리스트가 기준이 되어서 평균 점수 리스트에서
    # 해당하는 값이 몇 번째로 큰지 알 수 있다.
    # 이때 사용하는 것이 "index() 함수를 사용하는 것이다."
    # index 함수를 사용하면 자연스럽게 공동 등수 문제를 해결 할 수 있다.
    # ex) [75, 75, 40, 95, 95, 100, 20] 면 -> [100, 95, 95, 75, 75, 40, 20]
    # index는 중복 시 가장 앞의 원소만 선택하므로 95는 1번째, 75는 3번째 원소를 택한다.
    for i in avg:
        answer.append(arr.index(i)+1)
    


    return answer


solution([[80, 70], [70, 80], [30, 50], [90, 100], [100, 90], [100, 100], [10, 30]])