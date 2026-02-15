def solution(sides):
    # case를 2가지로 나눈다.
    # 1. 나머지 한 변이 가장 길거나
    # 2. 가장 긴 변이 sides 안에 존재하거나

    bigSides = 0    # 주어진 변 2개중 큰거
    smallSides = 0  # 작은거


    # 1. 나머지 한 변이 가장 길다고 가정
    sumSides = sides[0]+sides[1]

    # 긴 변 구하는 로직
    if sides[0]>sides[1]:
        bigSides = sides[0]
        smallSides = sides[1]
    else:
        bigSides = sides[1]
        smallSides = sides[0]


    cnt1 = 0
    numCase1 = bigSides+1   # 가장 긴 변 생성
    while numCase1<sumSides:    # 가장 긴 변이 나머지 변의 합보다 작으면 cnt+
        numCase1 += 1
        cnt1+=1
    

    # 2. 가장 긴 변이 sides 안에 존재한다.
    numCase2 = bigSides - smallSides +1 #주어진 변 중 긴 변보다 작으면서 그 합이 긴변보다는 큰 최소값으로 설정
    cnt2 = 1

    while numCase2<bigSides:    # 긴변보다 작을 때만 cnt+
        numCase2 += 1
        cnt2 += 1


    answer = cnt1+cnt2
    


    return answer
