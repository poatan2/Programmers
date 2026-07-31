def solution(a, b):
    answer = ''
    
    day=['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    total_day = 0
    
    for i in range(1,a):
        if i==1 or i==3 or i==5 or i==7 or i==8 or i==10 or i==12:
            total_day+=31
        elif i==2:
            total_day+=29
        else:
            total_day+=30
    
    total_day+=b

    answer = day[total_day%7-1] 
    
    
    return answer