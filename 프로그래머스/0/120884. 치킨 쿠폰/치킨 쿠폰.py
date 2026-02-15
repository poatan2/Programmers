def solution(chicken):
    answer = -1

    # 시켜먹은 치킨 수 = 쿠폰 수
    # 서비스 치킨은 쿠폰 10개
    coupon = chicken
    
    service = 0

    while coupon >= 10:
        #if coupon >= 10:
        # ** 그냥 서비스 치킨도 쿠폰을 한장 주니까 사실상 쿠폰 9개로 서비스 치킨을 먹을 수 있는 것이라
        # 생각하여 이렇게 했는데 됐다. **
        service +=1
        coupon -=9
        #print("빡",service,coupon)
    
        #if service >= 10:
         #   coupon +=1
          #  print("if",service,coupon)
        
    # print(service)
    answer = service
    
    return answer