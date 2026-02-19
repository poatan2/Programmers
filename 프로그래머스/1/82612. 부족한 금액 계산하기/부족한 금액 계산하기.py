def solution(price, money, count):
    answer = -1
    
    up_price = price
    total_price = 0
    
    for i in range(count):
        total_price += up_price
        up_price += price
        
    if money < total_price:
        return total_price-money
    else:
        answer = 0
    
    return answer   
