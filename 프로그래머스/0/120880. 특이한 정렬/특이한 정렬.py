def solution(numlist, n):
    answer = []

    # key 값을 기준으로 정렬해라
    # sort()함수가 실행되면서 안에 lambda의 x에 하나씩 배열의 원소 값이 넣어가면서 실행된다.
    # 튜플은 (값1, 값2) 처럼 묶인 데이터, 우선순위가 된다.
    # 2번째 우선순위인 -x는 x 앞에 -를 붙여 오름차순을 반대로 적용하는 효과를 보여줌
    # ex) 3 vs 5 => 3, 5   /  -3 vs -5  => -5 -3 이런식으로
    numlist.sort(key=lambda x: (abs(x - n),-x))
    answer = numlist


    return answer
