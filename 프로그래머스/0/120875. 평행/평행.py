def solution(dots):
    answer = 0
    
    # 일단 점 4개니까 직선이 만들어지는 경우는 총 6번의 경우가 있다.
    # 만든 두 직선이 평행하려면
    # " 두 직선의 기울기가 같아야 한다. "

    # 기울기 : y2-y1 / x2-x1 = y4-y3 / x4-x3

    # 위와 같은 식으로 검사하면 분모가 0 일때 프로그램 에러 뜰 가능성이 있다.

    # 따라서 아래 방법으로 기울기가 같은지 검사한다.
    # (y2 - y1) * (x4 - x3) == (y4 - y3) * (x2 - x1)

    if (dots[1][1]-dots[0][1]) * (dots[3][0]-dots[2][0]) == (dots[3][1]-dots[2][1]) * (dots[1][0]-dots[0][0]):
        answer = 1

    elif (dots[2][1]-dots[0][1]) * (dots[3][0]-dots[1][0]) == (dots[3][1]-dots[1][1]) * (dots[2][0]-dots[0][0]):
        answer = 1

    elif (dots[3][1]-dots[0][1]) * (dots[1][0]-dots[2][0]) == (dots[1][1]-dots[2][1]) * (dots[3][0]-dots[0][0]):
        answer = 1
        
    return answer