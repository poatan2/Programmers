def solution(n, m):
    answer = []
    
    gcd=0
    lcm=0
    
    temp=0
    # m에 더 큰 수가 오게 만들기
    if m<n:
        temp=m
        m=n
        n=temp
    
    # 최대 공약수 구하기
    for i in range(1,n+1):
        if n%i==0 and m%i==0:
            gcd=i
    answer.append(gcd)
    
    # 최소 공배수 구하기
    # n*m = gcd*lcm이라는 특성을 이용하여 최소 공배수를 구한다.
    lcm = (n*m)//gcd
    answer.append(lcm)
    
    
    return answer