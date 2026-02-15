def solution(lines):
    answer = 0
    
    # ----- 아래 주석은 나의 얘기지만 틀린 내용 ---- #
    # 3개의 선분 중 2개씩 빼서 비교?
    # 즉 경우의 수 3번으로??

    # 그리고 생각나는 거는 
    # 예를 들어 (2,5) (3,9) 면
    # 2 에서 5까지 가는 중에 (3,9)에서 만나는 지점이 있다면 거기서부터 카운팅해서 끝나는 곳까지하면 될 듯
    

    # ----- 여기가 진짜 -----#
    # hint for 제미나이
    # -100 ~ 100 까지의 지도를 만들고 거기에 카운팅 된 만큼 겹친거다
    # 그래서 2번이상 카운팅 된 곳은 겹쳐있는 곳이다.

    count_dict = {}
    for i in range(-100, 100):
        count_dict[i] = 0
    
    # 딕셔너리에 표시
    for i in range(3):
        for j in range(lines[i][0], lines[i][1]):
            count_dict[j] += 1
    
    # print(count_dict)

    # 겹치는 구간 찾기
    section = 0
    for i in range(-100, 100):
        if count_dict[i]>=2:
            section+=1

    answer = section

    return answer
    

