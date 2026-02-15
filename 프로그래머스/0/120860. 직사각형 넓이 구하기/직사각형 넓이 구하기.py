def solution(dots):
    answer = 0
    
    max_x = dots[0][0]
    min_x = dots[0][0]
    
    max_y = dots[0][1]
    min_y = dots[0][1]
    
    for x,y in dots:
        if max_x < x:
            max_x = x
        elif min_x > x:
            min_x = x
        if max_y < y:
            max_y = y
        elif min_y > y:
            min_y = y
    
    width = max_x - min_x
    length = max_y - min_y
    
    answer = width*length
    
    return answer